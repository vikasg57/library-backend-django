from .models import UserProfile

from django.contrib.auth.models import User


class UserHandler:
    def create_user(self, first_name, last_name, email, password):
        user = UserProfile.objects.filter(UserProfile__email=email)
        print(user)
        if not user:
            user = User.objects.create_user(username=email,
                                            email=email,
                                            first_name=first_name,
                                            last_name=last_name,
                                            password=password)
            UserProfile.objects.create(UserProfile=user)
            return {
                'first_name': user.first_name,
                'email': user.email
            }
        else:
            return {'message': "user already exist"}
