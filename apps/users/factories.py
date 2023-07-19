from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
import factory


from . import models


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tblcontact

    ntype = factory.Iterator(models.Tbltypecontact.objects.all())
    ntypesous = factory.Iterator(models.Tbltypecontactsous.objects.all())
    cnom = factory.Faker('last_name')
    cprenom = factory.Faker('first_name')
    cemail = factory.Faker('email')
    blntps = True
    blntvq = True
    bdistributeur = False
    baccesreservationgolibro = False
    # nLangue 
    # nFrequence

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tblcontactsecondaire

    cemail = factory.Faker('email')
    cnom = factory.Faker('last_name')
    cprenom = factory.Faker('first_name')
    password = factory.Faker('password')
    is_superuser = False
    is_staff = False
    ncontact = factory.SubFactory(ContactFactory)
    blnenvoimsg = False
    blnaccesftp = False
    blnaccesextranet = False
    blnaccesadmin = False
    msrepl_tran_version = factory.Faker('pystr')
    blnaccesfacturation = False
    blnaccessepreuve = False
    blnupdatemainserver = False
    blnaccessbv = False
    blnaccessbvadmin = False
    blnaccessbvacheteur = False
    blnaccessbvutilisateur = False
    blnacceptcontract = False

