import factory
from factory import Sequence
from factory.django import DjangoModelFactory

from kikeou.models.person import Person
from tests.factories.cycle import CycleFactory

__all__ = ["PersonFactory"]


class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person

    cycle = factory.SubFactory(CycleFactory)
    user = None
    first_name = Sequence(lambda n: f"Toto-{n}")
    last_name = Sequence(lambda n: f"Tutu-{n}")
    phone = ""
    email = ""
    diet_type = ""
