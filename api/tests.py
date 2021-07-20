from django.contrib import auth
from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import RequestFactory, TestCase

from api.views import authentication

USER_MODEL = get_user_model()

class TestLoginView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_can_login(self):
        data = {'email' : 'pendenquejohn@gmail.com', 'password': 'touparet'}
        request = self.factory.post(reverse('api:login'), data)
        response = authentication.Login.as_view()(request)
        # Since the user does not exist, this should
        # receive a 202
        self.assertEqual(response.status_code, 202)
        