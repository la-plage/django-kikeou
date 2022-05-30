from datetime import date

from factory import Sequence
from factory.django import DjangoModelFactory

from kikeou.models import Cycle

__all__ = ["CycleFactory"]


class CycleFactory(DjangoModelFactory):
    class Meta:
        model = Cycle

    name = "Festival 2022"
    start_date = date(2022, 8, 1)
    end_date = date(2022, 8, 5)
