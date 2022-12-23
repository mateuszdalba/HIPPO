#Signals in Django
#Notice that we have to go to the admin page to create a profile whenever a user is created,
#  but we don't wanna do that every now and then. It would be great if we can create the profiles 
# automatically when a new user is created. To do this we use signals.


from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()