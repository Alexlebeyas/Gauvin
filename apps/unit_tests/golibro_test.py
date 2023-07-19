from rest_framework.test import APITestCase
from apps.users.models import Tbltypecontact, Tbltypecontactsous

class GolibroTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Tbltypecontact.objects.create(ictype=1, cdescription='Client', cdescriptionan='Client', lsysteme=1)
        Tbltypecontact.objects.create(ictype=2, cdescription='Fournisseur', cdescriptionan='Supplier', lsysteme=1)
        Tbltypecontact.objects.create(ictype=3, cdescription='Employé', cdescriptionan='Employee', lsysteme=1)
        Tbltypecontact.objects.create(ictype=4, cdescription='Prospect', cdescriptionan='Prospect', lsysteme=1)

        Tbltypecontactsous.objects.create(ictype=1, cdescription='(aucun)', cdescriptionan='(none)')
        Tbltypecontactsous.objects.create(ictype=5, cdescription='Gouvernement', cdescriptionan='Supplier')
        Tbltypecontactsous.objects.create(ictype=6, cdescription='municipale', cdescriptionan='municipale')
        Tbltypecontactsous.objects.create(ictype=7, cdescription='scolaire', cdescriptionan='scolaire')
