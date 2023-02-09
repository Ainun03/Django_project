from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Custumer
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def custumer_profile(sender, instance, created, **kwargs):
    if created:
        grup = Group.objects.get(name='custumer')
        instance.groups.add(grup)
        Custumer.objects.create(
            user=instance,
            name=instance.username
            )