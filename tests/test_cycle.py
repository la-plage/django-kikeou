from datetime import date

from django.test import TestCase
from django.urls import reverse

from tests.factories import CycleFactory, SuperUserFactory


class CycleTestCase(TestCase):
    @staticmethod
    def test_save_cycle():
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
            self.client.get(reverse("admin:kikeou_cycle_changelist")).status_code, 200
        )
        self.assertEqual(
            self.client.get(reverse("admin:kikeou_cycle_add")).status_code, 200
        )
        self.assertEqual(
            self.client.get(
                reverse("admin:kikeou_cycle_delete", args=[CycleFactory().id])
            ).status_code,
            200,
        )
        self.assertEqual(
            self.client.get(
                reverse("admin:kikeou_cycle_change", args=[CycleFactory().id])
            ).status_code,
            200,
        )

    def test_active_cycle_is_set_automatically(self):
        # First cycle instance has is_the_active_one=True forced automatically
        self.assertTrue(CycleFactory(is_the_active_one=False).is_the_active_one)

        # Other cycle instances have is_the_active_one=False as default
        self.assertFalse(CycleFactory().is_the_active_one)

    def test_cant_have_more_than_one_active_cycle(self):
        first_cycle = CycleFactory(is_the_active_one=True)
        self.assertTrue(first_cycle.is_the_active_one)

        # Create a second cycle with is_the_active_one=True
        self.assertTrue(CycleFactory(is_the_active_one=True).is_the_active_one)

        # Check that first cycle has been automatically set to false
        first_cycle.refresh_from_db()
        self.assertFalse(first_cycle.is_the_active_one)
