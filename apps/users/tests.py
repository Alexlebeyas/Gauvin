from django.urls import include, path, reverse
from rest_framework import status
from django.contrib.auth.hashers import make_password
from apps.unit_tests.golibro_test import GolibroTestCase
from . import factories

# class GolibroTestCase(GolibroTestCase):
#     @classmethod
#     def setUpTestData(cls):
#         models.Tbltypecontact.objects.create(ictype=1, cdescription='Client', cdescriptionan='Client', lsysteme=1)
#         models.Tbltypecontact.objects.create(ictype=2, cdescription='Fournisseur', cdescriptionan='Supplier', lsysteme=1)
#         models.Tbltypecontact.objects.create(ictype=3, cdescription='Employé', cdescriptionan='Employee', lsysteme=1)
#         models.Tbltypecontact.objects.create(ictype=4, cdescription='Prospect', cdescriptionan='Prospect', lsysteme=1)

#         models.Tbltypecontactsous.objects.create(ictype=1, cdescription='(aucun)', cdescriptionan='(none)')
#         models.Tbltypecontactsous.objects.create(ictype=5, cdescription='Gouvernement', cdescriptionan='Supplier')
#         models.Tbltypecontactsous.objects.create(ictype=6, cdescription='municipale', cdescriptionan='municipale')
#         models.Tbltypecontactsous.objects.create(ictype=7, cdescription='scolaire', cdescriptionan='scolaire')


class LoginTest(GolibroTestCase):

    def setUp(self):
        self.password = 'secret'
        self.user = factories.UserFactory.create(password=make_password(self.password))
        self.login_endpoint = reverse('tokens_obtain_pair')

    def test_invalid_user_login_response(self):
        """Valid email and password gets 400 response status"""
        data = {'cemail': self.user.cemail, 'password': 'boya'}
        response = self.client.post(self.login_endpoint, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_invalid_playload_login_get_error(self):
        """Invalid payload get 400 response status"""
        data = {'email': self.user.cemail, 'password': self.password}
        response = self.client.post(self.login_endpoint, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_credentials_login_get_error(self):
        """Invalid credentials get 400 response status"""
        data = {'cemail': 'wrongemail', 'password': self.password}
        response = self.client.post(self.login_endpoint, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_method_login_get_error(self):
        """Invalid method get 405 response status"""
        data = {'email': self.user.cemail, 'password': self.password}
        response = self.client.get(self.login_endpoint, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)    
        

    def test_valid_user_login_response_with_tokens(self):
        """Valid email and password gets 200 response status and access and refresh tokens"""
        data = {'cemail': self.user.cemail, 'password': self.password}
        response = self.client.post(self.login_endpoint, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)