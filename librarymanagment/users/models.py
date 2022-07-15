from django.db import models

from django.contrib.auth.models import User

import uuid
# Create your models here.


class UserProfile(models.Model):
    UserProfile = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.UserProfile.email
