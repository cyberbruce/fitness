from django import forms
from . import models

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = models.Workout
        fields = ['name', 'workout_datetime', 'duration', 'effort', 'description']
        widgets = {
          'name': forms.TextInput(attrs={ 'autofocus': True }),
          'workout_datetime': forms.DateTimeInput(attrs={'data-controller': 'datepicker', 'data-datepicker-time': 'true' })
        }