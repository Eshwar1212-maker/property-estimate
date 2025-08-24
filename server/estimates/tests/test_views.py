# estimates/tests/test_views.py
import pytest
from django.urls import reverse
from estimates.models import PropertyInquiry, PropertyEstimate


@pytest.mark.django_db
def test_estimate_view_creates_inquiry_and_redirects(client, monkeypatch):
    async def fake_generate(*args, **kwargs):
        from estimates.services.property_estimate import PropertyEstimateResponse

        return PropertyEstimateResponse(
            project_name="Mocked",
            project_description="Fake response",
            estimated_net_cash_flow=123,
            estimated_revenue=456,
            estimated_cost=333,
        )

    monkeypatch.setattr("estimates.views.generate_estimate", fake_generate)

    response = client.post(
        reverse("estimate_api"),
        {
            "address": "789 Oak St",
            "lot_size_acres": "3.5",
            "user_context": "Testing",
        },
    )

    assert response.status_code == 302  # redirect
    assert PropertyInquiry.objects.count() == 1
    assert PropertyEstimate.objects.count() == 1
