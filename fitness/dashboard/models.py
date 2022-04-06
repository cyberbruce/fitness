from django.db import models
from django.db.models.query_utils import Q
from django.contrib.auth.models import User
from django.forms import ValidationError
from base import FitnessModel
from django.db.models import Deferrable


class Profile(FitnessModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Weight(FitnessModel):
    lbs = models.DecimalField(decimal_places=2, max_digits=5)
    entry_date = models.DateTimeField(null=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="weights"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["entry_date", "profile"],
                name="unique_weight_by_day_for_user_profile",
            )
            
        ]

    def clean(self):
        self.validate_unique()
        super(self.__class__).clean()
        
  