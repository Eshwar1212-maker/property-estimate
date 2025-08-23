# services.py
import json
from pydantic import BaseModel, ValidationError
from django.conf import settings
from openai import AsyncOpenAI

class PropertyEstimateResponse(BaseModel):
    project_name: str
    project_description: str
    estimated_net_cash_flow: float
    estimated_revenue: float
    estimated_cost: float

async def generate_estimate(address: str, lot_size_acres: float, user_context: str) -> PropertyEstimateResponse:
    if not getattr(settings, "OPENAI_API_KEY", None):
        raise RuntimeError("OPENAI_API_KEY not configured")

    client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    prompt = (
        "You are a property valuation assistant. Given the address, lot size in acres, "
        "and optional context, produce a concise valuation.\n"
        "Return ONLY a single JSON object with exactly these keys:\n"
        "  project_name (string), project_description (string),\n"
        "  estimated_net_cash_flow (number), estimated_revenue (number), estimated_cost (number).\n"
        "Do not include any markdown, code fences, or commentary.\n\n"
        f"Address: {address}\n"
        f"Lot size (acres): {lot_size_acres}\n"
        f"User context: {user_context or 'N/A'}\n"
    )

    resp = await client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        temperature=0.2,
    )

    # Robustly extract text across SDK variants
    text = getattr(resp, "output_text", None)
    if not text:
        try:
            # Some versions: resp.output[0].content[0].text
            text = resp.output[0].content[0].text
        except Exception:
            # Last-resort: stringify for debugging
            raise RuntimeError("Could not extract model text output from OpenAI response")

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Model did not return valid JSON: {e}\nRaw: {text[:400]}")

    try:
        return PropertyEstimateResponse(**data)
    except ValidationError as e:
        raise RuntimeError(f"Pydantic validation failed: {e}\nData: {data}")
