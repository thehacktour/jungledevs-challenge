from django.db import models
import uuid

class UserModel(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField('Username', max_length=50)
    password = models.CharField('Password', max_length=50)
    points = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.username

