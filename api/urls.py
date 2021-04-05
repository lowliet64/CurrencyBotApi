from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers


urlpatterns = [
    path('login/', obtain_auth_token, name='get_token'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('depositar/', views.DepositoView.as_view(), name='deposito'),
]
