
from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser,Account,Activity
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
# Create your views here.

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class RegisterView(APIView):
    def post(self,request):
            try:
                CustomUser.objects.get(username=request.data['username'])
                return Response({'message':'Ja existe um usuario com esse username'},status=422)
            except:
                new_user = CustomUser(username=request.data['username'])
                new_user.set_password(request.data['password'])
                account  = Account(owner=new_user)
                new_user.save()
                account.save()
                return Response({'username':new_user.username},status=200)
       
class DepositoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        key=request.headers['Authorization'][6:]
        user =Token.objects.get(key=key).user
        account = Account.objects.get(owner=user)
        old_balance= account.balance
        account.balance+=200
        new_balance =account.balance
        account.save()
        activity = Activity(account=account,owner=owner,old_value=str(old_value),new_value=str(old_value))
        return Response({'message':'deposito executado com sucesso','old_balance':old_balance,'new_balance':new_balance})