from django import forms
from . import models

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = models.Workout
        fields = ['name', 'workout_datetime', 'duration']
        widgets = {
          'name': forms.TextInput(attrs={ 'autofocus': True }),
          'workout_datetime': forms.TextInput(attrs={'type': 'date'})
        }