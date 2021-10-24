from django.db import models
import uuid

class PointsUser(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    points = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.points

class UserModel(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField('Username', max_length=50)
    password = models.CharField('Password', max_length=50)
    points = models.ForeignKey(PointsUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

