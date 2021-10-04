from django.test import TestCase
from rest_framework import status
from app.user.models import UserModel
from django.contrib.auth.models import User

class ApiTestCase(TestCase):
    def test_inicial(self):
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)

class TestGeneroEndpoint(TestCase):
    def setUp(self) -> None:
        self.url = f"/api/oficial/user/"
        super(TestGeneroEndpoint, self).setUp()

    def test_zinho(self):
        resp = self.client.get(self.url)
        self.assertFalse(status.is_success(resp.status_code))


class MoreOneTest(TestCase):
    fixtures = ["app/fixtures/usuario_lindo.json"]

    def test_should_create_group(self):
        fixtures = UserModel.objects.get(pk=1)
        self.assertEqual(fixtures.username, "smallpanda717")


class MoreTwoTest(TestCase):
    def test_usuario_nome(self):
        user = User.objects.create_user("Haki")
        assert user.username == "Haki"

    def test_senha(db) -> None:
        user = User.objects.create_user("A")
        user.set_password("secret")
        assert user.check_password("secret") is True

    def test_senha_falsa(db) -> None:
        user = User.objects.create_user("A")
        user.set_password("secret")
        user.set_unusable_password()
        assert user.check_password("secret") is False
