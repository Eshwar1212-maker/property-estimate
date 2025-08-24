# estimates/tests/test_models.py
import pytest
from estimates.models import PropertyInquiry, PropertyEstimate


@pytest.mark.django_db
def test_property_inquiry_and_estimate_creation():
    inquiry = PropertyInquiry.objects.create(
        address="123 Main St", lot_size_acres=1.5, user_context="Residential"
    )
    estimate = PropertyEstimate.objects.create(
        inquiry=inquiry,
        project_name="Test Project",
        project_description="Simple test description",
        estimated_net_cash_flow=1000,
        estimated_revenue=2000,
        estimated_cost=1000,
        raw_response={"mock": "data"},
    )
    assert estimate.inquiry.address == "123 Main St"
    assert estimate.estimated_net_cash_flow == 1000
