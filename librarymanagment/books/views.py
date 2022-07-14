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
        author_name = request.data.get('author_name')
        data = BookHandler().create_books_and_author_map(
            book_name, description,
            year, author_name)
        return HttpResponse(json.dumps(data))

    def put(self, request, *args, **kwargs):
        book_map_id = request.GET.get('book_map_id')
        book_name = request.data.get('book_name')
        description = request.data.get('description')
        year = request.data.get('year')
        author_name = request.data.get('author_name')
        print(book_map_id)
        data = BookHandler().update_books_and_author_map(
            book_name, description,
            year, author_name, book_map_id)
        return HttpResponse(json.dumps(data))

    def delete(self, request, *args, **kwargs):
        book_map_id = request.GET.get('book_map_id')
        data = BookHandler().delete_books_and_author_map(book_map_id)
        return HttpResponse(json.dumps(data))


