from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class CustomUser(AbstractUser):
    pass


class Account(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    balance = models.FloatField(default=0.0, blank=True)
    currency = models.CharField(default='USD',blank=False,max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Activity(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    conta = models.ForeignKey(Account, on_delete=models.PROTECT)
    old_value = models.CharField(blank=True,max_length=80)
    new_Value = models.CharField(blank=True,max_length=80)
    transacao = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if(created):
        Token.objects.create(user=instance)
