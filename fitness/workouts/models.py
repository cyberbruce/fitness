from django.db import models
from dashboard.models import Profile


class Workout(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="workouts"
    )
    name = models.CharField(max_length=255)
    workout_datetime = models.DateTimeField()
    duration = models.IntegerField(default=0)
    effort = models.IntegerField(default=5, choices=((x, str(x)) for x in range(1, 11)))

    def pct(self):
        return int(round(100.0 * (self.effort / 10.0), 0))
