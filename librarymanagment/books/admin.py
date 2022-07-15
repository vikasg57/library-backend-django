from django.contrib import admin

from .models import Author, Book, BookAuthorMapping, UserProfile


class BaseModelAdmin(admin.ModelAdmin):

    default_readonly_fields = ("created_at", "uuid")
    ordering = ("-created_at",)
    search_fields = ("uuid",)
    readonly_fields = ("uuid", "created_at", "updated_at")
    foreign_key_fields = ()


@admin.register(Book)
class BookAdminClass(BaseModelAdmin):
    search_fields = ("book_name",)
    list_display = ("book_name", "year")


@admin.register(Author)
class AuthorAdminClass(BaseModelAdmin):
    search_fields = ("author_name",)
    list_display = ("author_name", "uuid")


@admin.register(BookAuthorMapping)
class BookAuthorMappingAdmin(BaseModelAdmin):
    search_fields = ("author__author_name", "book__book_name")
    list_display = ("book", "author")


@admin.register(UserProfile)
class UserProfileAdmin(BaseModelAdmin):
    list_display = ("UserProfile", "is_admin")
