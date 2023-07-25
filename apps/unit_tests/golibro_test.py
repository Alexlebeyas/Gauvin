from rest_framework.test import APITestCase
from apps.users.models import ContactType, ContactSubType

class GolibroTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        ContactType.objects.create(id=1, description='Client', description_en='Client', is_system=1)
        ContactType.objects.create(id=2, description='Fournisseur', description_en='Supplier', is_system=1)
        ContactType.objects.create(id=3, description='Employé', description_en='Employee', is_system=1)
        ContactType.objects.create(id=4, description='Prospect', description_en='Prospect', is_system=1)

        ContactSubType.objects.create(id=1, description='(aucun)', description_en='(none)')
        ContactSubType.objects.create(id=5, description='Gouvernement', description_en='Supplier')
        ContactSubType.objects.create(id=6, description='municipale', description_en='municipale')
        ContactSubType.objects.create(id=7, description='scolaire', description_en='scolaire')

    def get(self, *args, **kwargs):
        return self.client.get(secure=True, *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.client.post(secure=True, *args, **kwargs)
