from django.urls import include, path, reverse
from rest_framework import status
from django.contrib.auth.hashers import make_password

from apps.unit_tests.golibro_test import GolibroTestCase
from apps.users import factories


class LoginTest(GolibroTestCase):

    password = "secret"
    login_endpoint = reverse("token_get")
    check_endpoint = reverse("sanity_check")

    def setUp(self):
        self.user = factories.UserFactory.create(password=make_password(self.password))

    def test_invalid_user_login_response(self):
        """Valid email and password gets 400 response status"""
        data = {"email": self.user.email, "password": "boya"}
        response = self.post(self.login_endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_payload_login_get_error(self):
        """Invalid payload get 400 response status"""
        data = {"bip": self.user.email, "password": self.password}
        response = self.post(self.login_endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_credentials_login_get_error(self):
        """Invalid credentials get 400 response status"""
        data = {"email": "wrongemail", "password": self.password}
        response = self.post(self.login_endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_method_login_get_error(self):
        """Invalid method get 405 response status"""
        data = {"email": self.user.email, "password": self.password}
        response = self.get(self.login_endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_valid_user_login_response_with_tokens(self):
        """Valid email and password gets 200 response status and access and refresh tokens"""
        data = {"email": self.user.email, "password": self.password}
        response = self.post(self.login_endpoint, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("refresh", response.data)
        self.assertIn("access", response.data)

    def test_check_returns_ok(self):
        """check call my returns ok"""
        response = self.get(self.check_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("OK", response.data)
