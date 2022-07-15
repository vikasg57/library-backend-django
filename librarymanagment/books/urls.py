from django.urls import path

from .views import BookAuthorMappingViewSet,UserCreateViewSet, LoginViewSet, LogoutViewSet

urlpatterns = [
    path('books', BookAuthorMappingViewSet.as_view(), name='book'),
    path('signup/', UserCreateViewSet.as_view(), name='sign-up'),
    path('login/', LoginViewSet.as_view(), name='login'),
    path('logout/', LogoutViewSet.as_view(), name='logout')
]
