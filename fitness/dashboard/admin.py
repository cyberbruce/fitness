from django.contrib import admin
from . import models

class WeightAdmin(admin.ModelAdmin):
  model = models.Weight
  list_display = ('entry_date', 'lbs')
  

admin.site.register(models.Weight, WeightAdmin)
admin.site.register(models.Profile)
