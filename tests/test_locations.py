from django.test import TestCase

from tests.factories.locations import LocationFactory


class LocationTestCase(TestCase):
    def test_location_str(self):
        self.assertEqual(
            str(LocationFactory(name="hello world")),
            "hello world",
        )
