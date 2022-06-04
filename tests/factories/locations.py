import factory
from factory import Sequence
from factory.django import DjangoModelFactory

from kikeou.models.locations import Accommodation, Location
from tests.factories.cycles import CycleFactory

__all__ = ["AccommodationFactory", "LocationFactory"]


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    cycle = factory.SubFactory(CycleFactory)
    name = Sequence(lambda n: f"Location #{n}")
    street = ""
    zip_code = ""
    city = ""
    contact = None


class AccommodationFactory(DjangoModelFactory):
    class Meta:
        model = Accommodation

    location = factory.SubFactory(
        LocationFactory, name=Sequence(lambda n: f"Accommodation #{n}")
    )
