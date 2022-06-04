from django.test import TestCase

from kikeou.models.locations import Accommodation
from tests.factories.locations import AccommodationFactory

# FIXME: try to find a solution to have an independent model inheriting from abstract and script tests.
#        In the meantime, we use here Accommodation model that inherit from LocationDependentAbstract.


class LocationDependentTestCase(TestCase):
    def test_location_dependent_str(self):
        self.assertEqual(
            str(AccommodationFactory(location__name="hello world")),
            "hello world",
        )

    def test_location_dependent_queryset_catch_related_location(self):
        AccommodationFactory()
        accommodation = Accommodation.objects.first()
        with self.assertNumQueries(0):
            accommodation.location.name
