from django.contrib import admin
from . import models

class WorkoutAdmin(admin.ModelAdmin):
 
  model = models.Workout
  list_display = ('id', 'name', 'workout_datetime', 'duration', 'effort', )


admin.site.register(models.Workout, WorkoutAdmin)