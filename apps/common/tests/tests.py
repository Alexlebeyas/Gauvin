from django.urls import reverse
from rest_framework import status

from apps.common.tests.golibro import GolibroTestCase


class CommonTest(GolibroTestCase):

    check_endpoint = reverse("sanity_check")

    def test_check_returns_ok(self):
        """check call my returns ok"""
        response = self.get(self.check_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("OK", response.data)
