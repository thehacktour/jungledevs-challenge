from django.db import models

class UserModel(models.Model):

    STATUS_OPCOES = (
        ('DRAFT','DRAFT'),
        ('TRASH','TRASH'),
        ('PUBLISHED','PUBLISHED'),
    )
    
    name = models.CharField('Name', max_length=50)
    imported_t = models.DateTimeField(auto_now=True)
    status = models.CharField('Status', choices=STATUS_OPCOES , default="DRAFT")
    age = models.PositiveBigIntegerField('Age', default=18)

    def __str__(self):
        return self.name