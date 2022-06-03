import factory
from factory.django import DjangoModelFactory

from kikeou.models.company import Company
from tests.factories.cycle import CycleFactory

__all__ = ["CompanyFactory"]


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    cycle = factory.SubFactory(CycleFactory)
    name = factory.Sequence(lambda n: f"Company #{n}")
