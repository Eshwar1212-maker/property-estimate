from django.urls import path
from .views import PropertyEstimateView
from django.http import HttpResponse

# quick inline view for homepage
def home(request):
    return HttpResponse("Welcome to the Property Estimate Tool")

urlpatterns = [
    path("", home, name="home"),
    path("api/estimate/", PropertyEstimateView.as_view(), name="property-estimate"),
]
