from django.conf import settings
from django.contrib.auth.models import User
from django.core import signals
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username=models.CharField(max_length=70,)
    nickname=models.CharField(max_length=120)
    picture=models.ImageField(null=True, blank=True)
    bio=models.TextField(null=True, blank=True)
    birthday=models.DateField(null=True, blank=True)
    cover=models.ImageField(null=True, blank=True)
    follows = models.ManyToManyField('Profile', related_name='followed_by',  blank=True)

    def __str__(self):
        return self.username or 'New User'





@receiver(post_save, sender=User)
def create_profile(sender, instance,created, **kwargs):
    """signal to auto create a profile instance for each user instance created"""
    if created:
        Profile.objects.create(user=instance, username=instance.username, nickname=instance.username)

    instance.profile.save()
