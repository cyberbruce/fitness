from django.urls import path
from . import views


app_name = "workouts"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("new", views.CreateWorkoutView.as_view(), name="create_workout"),
    path("update/<int:pk>", views.UpdateWorkoutView.as_view(), name="update_workout"),
    path("delete/<int:pk>", views.DeleteWorkoutView.as_view(), name="delete_workout"),
    
]
