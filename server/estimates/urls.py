from django.urls import path
from .views import PropertyEstimateView
from django.http import HttpResponse
from .views import estimate_form, PropertyEstimateView, estimate_result, estimate_results_list

# quick inline view for homepage
def home(request):
    return HttpResponse("Welcome to the Property Estimate Tool")

urlpatterns = [
    path("", estimate_form, name="estimate_form"),
    path("api/estimate/", PropertyEstimateView.as_view(), name="estimate_api"),
    path("results/", estimate_results_list, name="estimate_results_list")
]