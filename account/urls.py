
from account.views.account import AccountRegisterView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

    path('register/', AccountRegisterView.as_view()),
    path('login/', obtain_auth_token)
]
