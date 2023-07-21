from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
import factory


from . import models


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    contact_type = factory.Iterator(models.ContactType.objects.all())
    sous_contact_type = factory.Iterator(models.ContactSousType.objects.all())
    last_name = factory.Faker('last_name')
    first_name = factory.Faker('first_name')
    email = factory.Faker('email')
    gst = True
    qst = True
    distributer = False
    golibro_booking_access = False

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    email = factory.Faker('email')
    last_name = factory.Faker('last_name')
    first_name = factory.Faker('first_name')
    password = factory.Faker('password')
    is_superuser = False
    is_staff = False
    contact = factory.SubFactory(ContactFactory)
    send_message = False
    ftp_access = False
    extranet_access = False
    is_staff = False
    msrepl_tran_version = factory.Faker('pystr')
    billing_access = False
    examination_access = False
    update_main_server = False
    bv_access = False
    bv_admin_access = False
    bv_buyer_access = False
    bv_user_access = False
    accept_contract = False

