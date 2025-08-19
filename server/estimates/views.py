from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import PropertyInquiry, PropertyEstimate

@method_decorator(csrf_exempt, name="dispatch")
class PropertyEstimateView(View):
    async def post(self, request):
        try:
            data = json.loads(request.body)

            # Extract inputs
            address = data.get("address")
            lot_size_acres = data.get("lot_size_acres")
            user_context = data.get("user_context", "")

            # Save inquiry
            inquiry = await PropertyInquiry.objects.acreate(
                address=address,
                lot_size_acres=lot_size_acres,
                user_context=user_context
            )

            # For now, fake an AI response by echoing back values
            estimate = await PropertyEstimate.objects.acreate(
                inquiry=inquiry,
                project_name="Placeholder Project",
                project_description="This is a test response",
                estimated_net_cash_flow=100000.00,
                estimated_revenue=150000.00,
                estimated_cost=50000.00,
                raw_response={"mock": "test"}
            )

            return JsonResponse({
                "address": inquiry.address,
                "lot_size_acres": str(inquiry.lot_size_acres),
                "user_context": inquiry.user_context,
                "project_name": estimate.project_name,
                "project_description": estimate.project_description,
                "estimated_net_cash_flow": str(estimate.estimated_net_cash_flow),
                "estimated_revenue": str(estimate.estimated_revenue),
                "estimated_cost": str(estimate.estimated_cost),
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
