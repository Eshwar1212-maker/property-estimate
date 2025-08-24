import pytest
import asyncio
from estimates.services.property_estimate import generate_estimate, PropertyEstimateResponse

def test_generate_estimate_returns_response(monkeypatch):
    class FakeResponse:
        output_text = """{
            "project_name": "Mock",
            "project_description": "Desc",
            "estimated_net_cash_flow": 1,
            "estimated_revenue": 2,
            "estimated_cost": 1
        }"""

    class FakeClient:
        class responses:
            @staticmethod
            async def create(*args, **kwargs):
                return FakeResponse()

    monkeypatch.setattr(
        "estimates.services.property_estimate.AsyncOpenAI",
        lambda **kwargs: FakeClient()
    )

    result = asyncio.run(generate_estimate("addr", 1.0, "ctx"))

    assert isinstance(result, PropertyEstimateResponse)
    assert result.project_name == "Mock"
    assert result.estimated_net_cash_flow == 1
