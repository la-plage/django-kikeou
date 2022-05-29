from datetime import date

from django.test import TestCase
from kikeou.models.cycle import Cycle


class CycleTestCase(TestCase):
    def test_save_cycle(self):
        cycle = Cycle()
        cycle.name = "Best Festival 2022"
        cycle.start_date = date(2022, 8, 1)
        cycle.end_date = date(2022, 8, 2)
        cycle.save()

    def test_cant_set_end_date_before_start_date(self):
        cycle = Cycle()
        cycle.name = "Best Festival 2022"
        cycle.start_date = date(2022, 8, 2)
        cycle.end_date = date(2022, 8, 1)
        with self.assertRaises(ValueError):
            cycle.save()
