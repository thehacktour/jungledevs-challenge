from django.db import models

class UserModel(models.Model):
    
    name = models.CharField('Name', max_length=50)
    age = models.PositiveBigIntegerField('Age', default=18)

    def __str__(self):
        return self.name