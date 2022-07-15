from django.contrib import admin

from .models import UserProfile
# Register your models here.


class BaseModelAdmin(admin.ModelAdmin):

    default_readonly_fields = ('created_at', 'uuid')
    ordering = ('-created_at',)
    search_fields = ('uuid',)
    readonly_fields = ('uuid', 'created_at', 'updated_at')

    foreign_key_fields = ()


class UserProfileAdmin(BaseModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)

