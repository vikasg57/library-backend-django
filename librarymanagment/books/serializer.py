from rest_framework import serializers
from .models import (
    Author,
    Book,
    BookAuthorMapping
)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['uuid', 'book_name', 'description', 'year']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['uuid', 'author_name']


class BookAuthorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthorMapping
        fields = ['uuid',]