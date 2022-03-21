from django.urls import path
from . import views


appname = "dashboard"
urlpatterns = [
  path("", views.HomeView.as_view(), name="home")
]