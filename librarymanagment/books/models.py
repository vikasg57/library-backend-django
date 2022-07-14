import uuid
from django.db import models

# Create your models here.


class BaseModel(models.Model):

    class Meta:
        abstract = True

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,)
    updated_at = models.DateTimeField(auto_now_add=True)


class Book(BaseModel):
    book_name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name


class Author(BaseModel):
    author_name = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.author_name


class BookAuthorMapping(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='book')
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='author')

    def __str__(self):
        return self.book.book_name
