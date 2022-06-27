from django.test import TestCase
from django.urls import reverse


class ViewTestCase(TestCase):
    def test_dashboard_view_returns_200(self):
        self.assertEqual(self.client.get(reverse("kikeou:dashboard")).status_code, 200)
