
from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.


class Teste (View):
    template_name = 'api/teste.html'

    def get(self, request):
        return render(request, self.template_name)
