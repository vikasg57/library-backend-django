from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import UserProfile


class UserHandler:
    def create_user(self, first_name, last_name, email, password, is_admin):
        user = UserProfile.objects.filter(UserProfile__email=email)
        if not user:
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            UserProfile.objects.create(UserProfile=user, is_admin=is_admin)
            return {"first_name": user.first_name, "email": user.email}
        else:
            return {"message": "user already exist"}

    def login_user(self, request, username, password):
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return {"massage": "User logged in Successfully"}
        else:
            return {"message": "User not present please sign up first"}

    def logout_user(self, request):
        logout(request)
        return {"message": "User logged out"}
