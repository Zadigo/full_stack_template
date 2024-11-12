from django.test import TestCase

from django_seo.models import LegalBusiness


class TestLegalBusiness(TestCase):
    def setUp(self):
        params = {
            'legal_name': 'Company'
        }
        self.my_model = LegalBusiness.objects.create(**params)

    def test_my_model_creation(self):
        self.assertTrue(isinstance(self.my_model, LegalBusiness))
        self.assertEqual(self.my_model.__str__(), 'SEO version 0')

    def test_my_model_update(self):
        self.my_model.legal_name = 'Company 2'
        self.my_model.save()
        updated_model = LegalBusiness.objects.get(pk=self.my_model.pk)
        self.assertEqual(updated_model.legal_name, 'Company 2')

    def test_model_get_latest(self):
        item = LegalBusiness.objects.get_latest_version()
        self.assertEqual(item.legal_name, 'Company 2')

    def test_my_model_deletion(self):
        self.my_model.delete()
        with self.assertRaises(LegalBusiness.DoesNotExist):
            LegalBusiness.objects.get(pk=self.my_model.pk)
