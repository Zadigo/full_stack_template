from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


class AuthenticationMixin:
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.get(pk=1)
        cls.user.set_password('touparet')
        cls.user.save()

    def setUp(self):
        self.client = self.client_class()
        self.token = self._authenticate()

    def _authenticate(self):
        response = self.client.post(
            reverse('token_obtain_pair'),
            data={
                'email': 'lena.vivas@yopmail.com',
                'password': 'touparet'
            }
        )

        self.assertEqual(response.status_code, 200, 'Authentication failed')

        token = response.json().get('access')
        self.assertIsNotNone(token, 'Token retrieval failed')

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        return token


class TestSignup(APITestCase):
    def test_can_signup(self):
        response = self.client.post(
            reverse('api_accounts:signup'),
            data={
                'email': 'test@example.com',
                'firstname': 'Marie',
                'lastname': 'Gaumont',
                'username': 'marieg',
                'password1': 'touparet',
                'password2': 'touparet'
            }
        )
        self.assertEqual(response.status_code, 201)


class TestLogin(APITestCase):
    fixtures = ['users']

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.first()
        cls.user.set_password('touparet')
        cls.user.save()

    def test_can_authenticate(self):
        response = self.client.post(
            reverse('token_obtain_pair'),
            data={
                'email': 'lena.vivas@yopmail.com',
                'password': 'touparet'
            }
        )
        self.assertIsNotNone(response.json().get('access'))

    def test_can_get_profile(self):
        pass


class TestProfile(AuthenticationMixin, APITestCase):
    fixtures = ['users']

    def test_get_profile(self):
        response = self.client.get(
            reverse('api_accounts:profile')
        )
        self.assertEqual(response.status_code, 200)

    def test_update_profile(self):
        response = self.client.patch(
            reverse('api_accounts:profile'),
            data={
                'firstname': 'Marinne'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())

    def test_update_password(self):
        response = self.client.patch(
            reverse('api_accounts:profile'),
            data={
                'old_password': 'touparet',
                'password1': 'touparette',
                'password2': 'touparette'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())
