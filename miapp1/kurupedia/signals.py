from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver

@receiver(post_save,sender)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
#signals no funciona si en settings-installed apps ponemos solo "social"
#en lugar de eso tenemos que poner el patron complet 'social.apps.SocialConfig'
