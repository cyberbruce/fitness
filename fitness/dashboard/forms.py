from django.forms import ModelForm
from . import models
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class WeightForm(ModelForm):
  class Meta:
      model = models.Weight
      fields = ['lbs', 'entry_date']
      widgets = {
        'entry_date': DateInput(),
        'lbs': forms.TextInput(attrs={'autofocus':True})
      }