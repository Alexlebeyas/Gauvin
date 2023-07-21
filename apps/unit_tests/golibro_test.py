from rest_framework.test import APITestCase
from apps.users.models import ContactType, ContactSousType

class GolibroTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        ContactType.objects.create(ictype=1, cdescription='Client', cdescriptionan='Client', lsysteme=1)
        ContactType.objects.create(ictype=2, cdescription='Fournisseur', cdescriptionan='Supplier', lsysteme=1)
        ContactType.objects.create(ictype=3, cdescription='Employé', cdescriptionan='Employee', lsysteme=1)
        ContactType.objects.create(ictype=4, cdescription='Prospect', cdescriptionan='Prospect', lsysteme=1)

        ContactSousType.objects.create(ictype=1, cdescription='(aucun)', cdescriptionan='(none)')
        ContactSousType.objects.create(ictype=5, cdescription='Gouvernement', cdescriptionan='Supplier')
        ContactSousType.objects.create(ictype=6, cdescription='municipale', cdescriptionan='municipale')
        ContactSousType.objects.create(ictype=7, cdescription='scolaire', cdescriptionan='scolaire')
