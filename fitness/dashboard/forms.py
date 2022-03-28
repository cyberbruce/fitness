from django.forms import ModelForm
from . import models
from django import forms

 

class WeightForm(ModelForm):
  class Meta:
      model = models.Weight
      fields = ['lbs', 'entry_date']
      widgets = {
        'entry_date': forms.DateInput(attrs={'data-controller': 'datepicker'}),
        'lbs': forms.TextInput(attrs={'autofocus':True})
      }