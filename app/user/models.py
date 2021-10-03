from django.db import models
import uuid


class UserModel(models.Model):
    STATUS_OPCOES = (
        ('DRAFT', 'DRAFT'),
        ('TRASH', 'TRASH'),
        ('PUBLISHED', 'PUBLISHED'),
    )

    GENDER_OPCOES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )

    imported_t = models.DateTimeField(auto_now=True)
    status = models.CharField('Status', choices=STATUS_OPCOES, default="DRAFT", max_length=50)
    gender = models.CharField('Gender', choices=GENDER_OPCOES, default='MALE', max_length=50)
    title = models.CharField('Title', max_length=50)
    first = models.CharField('First', max_length=50)
    last = models.CharField('Last', max_length=50)
    street_number = models.IntegerField('Street Number', default=None)
    street_name = models.CharField('Street Name', max_length=50)
    city = models.CharField('City', max_length=50)
    state = models.CharField('State', max_length=50)
    postcode = models.IntegerField('Postcode', default=None)
    latitude = models.IntegerField('Latitude', default=None)
    longitude = models.IntegerField('Longitude', default=None)
    offset = models.TimeField('Offset', default=None)
    description = models.CharField('Description', max_length=50)
    email = models.EmailField('Email', max_length=50, default=None)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField('Username', max_length=50)
    password = models.CharField('Password', max_length=50)
    salt = models.CharField('Salt', max_length=50)
    md5 = models.CharField('MD5', max_length=100)
    sha1 = models.CharField('SHA1', max_length=100)
    sha256 = models.CharField('SHA256', max_length=100)
    dob_date = models.DateTimeField('Dob Date', default=None)
    dob_age = models.IntegerField('Dob Age', default=None)
    registered_date = models.DateTimeField('Registered Date', default=None)
    registered_age = models.IntegerField('Registered Age', default=18)
    phone = models.CharField('Phone', max_length=20)
    cell = models.CharField('Cell', max_length=20)
    id_name = models.CharField('ID Name', max_length=30)
    id_value = models.CharField('ID Value', max_length=50)
    picture_large = models.TextField('Picture Large', max_length=100)
    picture_medium = models.TextField('Picture Medium', max_length=70)
    picture_thumbnail = models.TextField('Picture Thumbnail', max_length=50)
    nat = models.CharField('Nat', max_length=30)
    seed = models.IntegerField('Seed', default=None)

    def __str__(self):
        return self.username
