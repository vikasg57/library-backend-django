import json

from django.shortcuts import render

from .book_handlers import BookHandler

from .user_handler import UserHandler

# Create your views here.
from django.http import JsonResponse, HttpResponse

from rest_framework.views import APIView


class BookAuthorMappingViewSet(APIView):

    def get(self, request, *args, **kwargs):
        print(request.user)
        user = request.user
        data = BookHandler().get_all_books_author_mapping(user)
        return HttpResponse(json.dumps(data))

    def post(self, request, *args, **kwargs):
        user = request.user
        book_name = request.data.get('book_name')
        description = request.data.get('description')
        year = request.data.get('year')
        author_names = request.data.get('authors')
        data = BookHandler().create_books_and_author_map(
            book_name, description,
            year, author_names, user)
        return HttpResponse(json.dumps(data))

    def put(self, request, *args, **kwargs):
        book_id = request.GET.get('book_id')
        book_name = request.data.get('book_name')
        description = request.data.get('description')
        year = request.data.get('year')
        data = BookHandler().update_books_and_author_map(
            book_name, description,
            year, book_id)
        return HttpResponse(json.dumps(data))

    def delete(self, request, *args, **kwargs):
        book_id = request.GET.get('book_id')
        data = BookHandler().delete_books_and_author_map(book_id)
        return HttpResponse(json.dumps(data))


class UserCreateViewSet(APIView):

    def post(self, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')
        is_admin = request.data.get('is_admin')
        data = UserHandler().create_user(first_name, last_name,
                                         email, password, is_admin)
        return HttpResponse(json.dumps(data))


class LoginViewSet(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('email')
        password = request.data.get('password')
        data = UserHandler().login_user(request, username, password)
        return HttpResponse(json.dumps(data))


class LogoutViewSet(APIView):
    def post(self, request, *args, **kwargs):
        data = UserHandler().logout_user(request)
        return HttpResponse(json.dumps(data))
