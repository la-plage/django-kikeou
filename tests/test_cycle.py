from datetime import date

from django.test import TestCase
from django.urls import reverse

from tests.factories import CycleFactory, SuperUserFactory


class CycleTestCase(TestCase):
    def test_save_cycle(self):
        cycle = CycleFactory()
        cycle.save()

    def test_cant_set_end_date_before_start_date(self):
        cycle = CycleFactory()
        cycle.start_date = date(2022, 8, 2)
        cycle.end_date = date(2022, 8, 1)
        with self.assertRaises(ValueError):
            cycle.save()

    def test_cycle_model_permissions(self):
        self.client.force_login(SuperUserFactory())
        self.assertEqual(
            self.client.get(reverse("admin:kikeou_cycle_add")).status_code, 200
        )
        self.assertEqual(
            self.client.get(reverse("admin:kikeou_cycle_changelist")).status_code, 200
        )
        self.assertEqual(
            self.client.get(
                reverse("admin:kikeou_cycle_change", args=[CycleFactory().id])
            ).status_code,
            200,
        )
