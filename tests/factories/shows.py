import factory

from kikeou.models.shows import Show, ShowType
from tests import factories

__all__ = ["ShowFactory", "ShowTypeFactory"]


class ShowTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShowType

    cycle = factory.SubFactory(factories.CycleFactory)
    name = factory.Sequence(lambda n: f"Wandering show #{n}")


class ShowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Show

    company = factory.SubFactory(factories.CompanyFactory)
    type = factory.SubFactory(ShowTypeFactory)
    code = factory.Sequence(lambda n: f"s-{n:04d}")
    name = factory.Sequence(lambda n: f"Show #{n}")
