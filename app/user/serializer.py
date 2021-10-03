from rest_framework import serializers

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            "imported_t",
            "status",
            "gender",
            "tittle",
            "first",
            "last",
            "street",
            "city",
            "state",
            "postcode",
            "latitude",
            "longitude",
            "offset",
            "description",
            "email",
            "username",
            "password",
            "salt",
            "md5",
            "sha1",
            "sha256",
            "dob_date",
            "dob_age",
            "registered_date",
            "registered_age",
            "phone",
            "cell",
            "id_name",
            "id_value",
            "picture_large",
            "picture_medium",
            "picture_thumbnail",
            "nat",
            "seed",
        )
