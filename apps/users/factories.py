from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
import factory
from factory.django import DjangoModelFactory

from apps.users import models


class ContactFactory(DjangoModelFactory):
    class Meta:
        model = models.Contact

    contact_type = factory.Iterator(models.ContactType.objects.all())
    sous_contact_type = factory.Iterator(models.ContactSubType.objects.all())
    last_name = factory.Faker('last_name')
    first_name = factory.Faker('first_name')
    email = factory.Faker('email')
    gst = True
    qst = True
    distributer = False
    golibro_booking_access = False

class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    email = factory.Faker('email')
    last_name = factory.Faker('last_name')
    first_name = factory.Faker('first_name')
    password = factory.Faker('password')
    is_superuser = False
    is_staff = False
    contact = factory.SubFactory(ContactFactory)
    can_send_message = False
    has_ftp_access = False
    has_extranet_access = False
    is_staff = False
    msrepl_tran_version = factory.Faker('pystr')
    has_billing_access = False
    has_examination_access = False
    has_update_main_server = False
    has_bv_access = False
    has_bv_admin_access = False
    has_bv_buyer_access = False
    has_bv_user_access = False
    can_accept_contract = False

