from django.test import TransactionTestCase
from django_analytics.models import AnalyticsVersion


class TestAnalyticsDatabase(TransactionTestCase):
    fixtures = ['analytics']

    def setUp(self):
        self.version1 = AnalyticsVersion.objects.create(
            google_analytics='G-EWXB23F'
        )

    def test_can_create(self):
        self.assertIsNotNone(self.version1)
        self.assertEqual(self.version1.google_analytics, 'G-EWXB23F')
