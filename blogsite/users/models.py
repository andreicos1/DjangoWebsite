from django.db import models
from django.contrib.auth.models import User as Default_user
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# Create your models here.
class User(Default_user):
    def __str__(self):
        return self.username


class Profile(models.Model):
    this_user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.this_user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(this_user=instance)
