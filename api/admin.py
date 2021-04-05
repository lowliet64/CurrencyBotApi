from django.contrib import admin
from .models import Account,CustomUser,Activity
from rest_framework.authtoken.models import Token
# Register your models here.
admin.site.register(Account)
admin.site.register(CustomUser)
admin.site.register(Activity)
admin.site.register(Token)