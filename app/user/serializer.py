from rest_framework import serializers

from .models import UserModel
from . import mensagens


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            "imported_t",
            "status",
            "gender",
            "title",
            "first",
            "last",
            "street_number",
            "street_name",
            "city",
            "state",
            "postcode",
            "latitude",
            "longitude",
            "offset",
            "description",
            "email",
            "uuid",
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

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)

        mandatory_fields = {
            "username": mensagens.MSG2.format(u"Usuario"),
            "password": mensagens.MSG2.format(u"Senha"),
            "email": mensagens.MSG2.format(u"Email"),
        }

        for key, value in mandatory_fields.items():
            self.fields[key].error_messages["required"] = value
            self.fields[key].error_messages["blank"] = value
            self.fields[key].error_messages["null"] = value

    def validate(self, data):
        if data.get('first') == 'Atilio':
            raise serializers.ValidationError(
                "Aqui não tem erro nenhum. Esse cara é lindo!"
            )
        if data.get('phone') == '00000000':
            raise serializers.ValidationError(
                "Esse número aí tá paia, hein?"
            )
        if data.get('latitude') and data.get('longitude') <=0:
            raise serializers.ValidationError(
                "Onde você ta, parceiro? Essa localização ai ta zoada!"
            )
        if data.get('password') == data.get('username'):
            raise serializers.ValidationError(
                "Isso daí ta errado, hein? Procura uma senha diferente, fião!"
            )
        if data.get('picture_medium') > data.get('picture.large'):
            raise serializers.ValidationError(
                "Hmmmm, que mundo é esse que a media é menor que a grande? "
            )
