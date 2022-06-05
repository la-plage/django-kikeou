import factory
from factory import Sequence
from factory.django import DjangoModelFactory

from kikeou.models.persons import Greeter, Person
from tests.factories.cycles import CycleFactory

__all__ = ["GreeterFactory", "PersonFactory"]


class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person

    cycle = factory.SubFactory(CycleFactory)
    user = None
    first_name = Sequence(lambda n: f"Toto #{n}")
    last_name = Sequence(lambda n: f"Dupond")
    phone = ""
    email = ""
    diet_type = ""


class GreeterFactory(DjangoModelFactory):
    class Meta:
        model = Greeter

    person = factory.SubFactory(
        PersonFactory, first_name=Sequence(lambda n: f"Greeter #{n}")
    )
