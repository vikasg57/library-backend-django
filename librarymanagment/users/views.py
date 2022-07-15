from django.shortcuts import render

from django.contrib.auth import login, logout

from rest_framework.views import APIView
from .models import UserProfile
# Create your views here.
import json

from .user_handler import UserHandler

from django.http import HttpResponse


class UserCreateViewSet(APIView):

    def post(self, request, *args, **kwargs):
        print("vikas")
        user = request.user
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')
        data = UserHandler().create_user(first_name, last_name, email, password)
        return HttpResponse(json.dumps(data))
