from rest_framework.response import Response
from account.serializers.account import AccountRegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework import generics


class AccountRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountRegisterSerializer
