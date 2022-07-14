from django.urls import path

from .views import BookAuthorMappingViewSet

urlpatterns = [
    path('books', BookAuthorMappingViewSet.as_view(), name='book'),
]
