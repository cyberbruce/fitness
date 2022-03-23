from django.db import models
from dashboard.models import Profile



class Workout(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="workouts")
  name = models.CharField(max_length=255)
  workout_datetime = models.DateField()
  duration = models.IntegerField(default=0)
  
