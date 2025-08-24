import json
from pydantic import BaseModel, ValidationError
from django.conf import settings
from pathlib import Path
from openai import AsyncOpenAI

PROMPT_PATH = (
    Path(__file__).resolve().parent / "prompts" / "property_estimate_prompt.txt"
)

class PropertyEstimateResponse(BaseModel):
    project_name: str
    project_description: str
    estimated_net_cash_flow: float
    estimated_revenue: float
    estimated_cost: float


async def generate_estimate(
    address: str, lot_size_acres: float, user_context: str
) -> PropertyEstimateResponse:
    if not getattr(settings, "OPENAI_API_KEY", None):
        raise RuntimeError("OPENAI_API_KEY not configured")

    client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    with open(PROMPT_PATH, "r") as f:
        base_prompt = f.read()

    prompt = base_prompt.format(
        address=address,
        lot_size_acres=lot_size_acres,
        user_context=user_context or "N/A",
    )
    resp = await client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        temperature=0.2,
    )

    text = getattr(resp, "output_text", None)

    if not text:
        try:
            text = resp.output[0].content[0].text
        except Exception:
            # Last-resort: stringify for debugging
            raise RuntimeError(
                "Could not extract model text output from OpenAI response"
            )

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Model did not return valid JSON: {e}\nRaw: {text[:400]}")

    try:
        return PropertyEstimateResponse(**data)
    except ValidationError as e:
        raise RuntimeError(f"Pydantic validation failed: {e}\nData: {data}")
