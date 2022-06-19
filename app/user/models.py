from django.db import models
import uuid

class UserModel(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('Email', max_length=100, default="")
    password = models.CharField('Password', max_length=50)

    def __str__(self):
        return self.username
