from django.urls import path

from .views import UserCreateViewSet

urlpatterns = [
    path('signup', UserCreateViewSet.as_view(), name='sign-up'),

]