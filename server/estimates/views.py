from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import PropertyInquiry, PropertyEstimate

class PropertyEstimateView(View):
    def post(self, request):
        try:
            # Extract from form POST
            address = request.POST.get("address")
            lot_size_acres = request.POST.get("lot_size_acres")
            user_context = request.POST.get("user_context", "")

            # Save inquiry
            inquiry = PropertyInquiry.objects.create(
                address=address,
                lot_size_acres=lot_size_acres,
                user_context=user_context
            )

            # Fake estimate for now
            PropertyEstimate.objects.create(
                inquiry=inquiry,
                project_name="Placeholder Project",
                project_description="This is a test response",
                estimated_net_cash_flow=100000.00,
                estimated_revenue=150000.00,
                estimated_cost=50000.00,
                raw_response={"mock": "test"}
            )

            # 👇 Redirect straight to list page, not a dynamic route
            return redirect("estimate_results_list")

        except Exception as e:
            return render(request, "estimates/form.html", {"error": str(e)})

def estimate_form(request):
    return render(request, "estimates/form.html")

def estimate_result(request, estimate_id):
    estimate = get_object_or_404(PropertyEstimate, id=estimate_id)
    return render(request, "estimates/result.html", {"estimate": estimate})

def estimate_results_list(request):
    estimates = PropertyEstimate.objects.all().order_by("-created_at")
    return render(request, "estimates/results.html", {"estimates": estimates})

