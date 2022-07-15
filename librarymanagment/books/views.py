import json

from django.shortcuts import render

from .book_handlers import BookHandler

# Create your views here.
from django.http import JsonResponse, HttpResponse

from rest_framework.views import APIView


class BookAuthorMappingViewSet(APIView):

    def get(self, request, *args, **kwargs):
        data = BookHandler().get_all_books_author_mapping()
        print(data)
        return HttpResponse(json.dumps(data))

    def post(self, request, *args, **kwargs):
        user = request.user
        book_name = request.data.get('book_name')
        description = request.data.get('description')
        year = request.data.get('year')
        author_names = request.data.get('authors')
        data = BookHandler().create_books_and_author_map(
            book_name, description,
            year, author_names)
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


