from django.urls import path
from . import views


app_name = "dashboard"
urlpatterns = [
  path("", views.HomeView.as_view(), name="home"),
  path("weight_checkin/", views.WeightCheckInView.as_view(), name="weight_checkin"),
  path("weights_summary", views.WeightsView.as_view(), name="weights_summary"),
  path("weights/<int:pk>", views.WeightView.as_view(), name="weight"),
  path("weights/<int:pk>/delete", views.destroy_weight, name="weight_destroy")
]