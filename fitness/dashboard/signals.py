from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from dashboard.models import Profile


@receiver(post_save, sender=User)
def user_added(sender, instance, created, **kwargs):
  """ After a user is created, add the profile record """
  if created:
    p = Profile(user=instance)
    p.save()

