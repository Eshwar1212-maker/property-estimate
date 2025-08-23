from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import PropertyInquiry, PropertyEstimate
from .services.property_estimate import generate_estimate


class PropertyEstimateView(View):
    async def post(self, request):
        try:
            address = request.POST.get("address")
            lot_size_acres = request.POST.get("lot_size_acres")
            user_context = request.POST.get("user_context", "")

            inquiry = await PropertyInquiry.objects.acreate(
                address=address,
                lot_size_acres=lot_size_acres,
                user_context=user_context,
            )

            ai = await generate_estimate(address, lot_size_acres, user_context)

            await PropertyEstimate.objects.acreate(
                inquiry=inquiry,
                project_name=ai.project_name,
                project_description=ai.project_description,
                estimated_net_cash_flow=ai.estimated_net_cash_flow,
                estimated_revenue=ai.estimated_revenue,
                estimated_cost=ai.estimated_cost,
                raw_response=ai.model_dump(),
            )

            return redirect("estimate_results_list")

        except Exception as e:
            import traceback

            print("ERROR in PropertyEstimateView.post:", str(e))
            traceback.print_exc()  # full stacktrace in logs
            return render(request, "estimates/form.html", {"error": str(e)})


def estimate_form(request):
    print("DEBUG: Rendering estimate_form template")
    return render(request, "estimates/form.html")


def estimate_result(request, estimate_id):
    print(f"DEBUG: Fetching estimate with id={estimate_id}")
    estimate = get_object_or_404(PropertyEstimate, id=estimate_id)
    return render(request, "estimates/result.html", {"estimate": estimate})


# views.py
def estimate_results_list(request):
    estimates = PropertyEstimate.objects.all().order_by("-created_at")
    return render(request, "estimates/results.html", {"estimates": estimates})
