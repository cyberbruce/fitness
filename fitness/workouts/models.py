from datetime import tzinfo
from django.db import models
from dashboard.models import Profile
from django.db.models.aggregates import Sum
from django.db.models.functions import TruncDay
from django.db.models import F
from base import FitnessModel
from django.utils import timezone
from django.db.models.functions import TruncDay


class WorkoutManager(models.Manager):
    def chart_data(self):
        """ Sum of intensity by workout date """
        return self.annotate(month=TruncDay("workout_datetime", tzinfo=timezone.tzinfo)).values("month").annotate(            
            total=Sum(F("duration")*F("effort"))
        )


class Workout(FitnessModel):
    objects = WorkoutManager()

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="workouts"
    )
    name = models.CharField(max_length=255)
    workout_datetime = models.DateTimeField()
    duration = models.IntegerField(default=0)
    effort = models.IntegerField(default=5, choices=((x, str(x)) for x in range(1, 11)))

    


    def pct(self):
        return int(round(100.0 * (self.effort / 10.0), 0))

    def intensity(self):
        return self.duration * self.effort
 
