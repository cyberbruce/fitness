from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Weight(models.Model):
    lbs = models.DecimalField(decimal_places=2, max_digits=5)
    entry_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
        if Weight.objects.filter(
            profile=self.profile, entry_date=self.entry_date
        ).exists():
            raise ValidationError(
                {"entry_date": "Sorry, a weight has already been entered for this."}
            )
