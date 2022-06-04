from django.db.utils import IntegrityError
from django.test import TestCase

from kikeou.models.abstracts.cycle_dependents import CycleDependentManager
from kikeou.models.companies import Company
from kikeou.models.cycles import Cycle
from tests.utils.cycles import create_5_cycles_batch

# FIXME: try to find a solution to have an independent model inheriting from abstract and script tests.
#        In the meantime, we use here Company model that inherit from CycleDependentAbstract.


class CycleDependentTestCase(TestCase):
    def test_get_default_cycle_without_any_cycle_record(self):
        self.assertEqual(Cycle.objects.all().count(), 0)
        self.assertIsNone(CycleDependentManager.get_default_cycle())

    def test_create_cycle_dependent_assigns_active_cycle_as_default(self):
        create_5_cycles_batch()
        self.assertEqual(
            Company.objects.create(name="toto").cycle.id,
            Cycle.objects.get_active().id,
        )

    def test_create_cycle_dependent_doesnt_assign_other_cycle_already_in_parameters(
        self,
    ):
        create_5_cycles_batch()
        first_cycle = Cycle.objects.filter(is_the_active_one=False).first()
        self.assertEqual(
            Company.objects.create(cycle=first_cycle, name="toto").cycle.id,
            first_cycle.id,
        )

    def test_instantiate_cycle_dependent_without_any_existing_cycle(self):
        self.assertEqual(Cycle.objects.all().count(), 0)
        with self.assertRaises(IntegrityError):
            Company().save()

    def test_save_new_cycle_dependent_assigns_active_cycle_as_default(self):
        create_5_cycles_batch()
        cycle_dependent = Company()
        cycle_dependent.name = "toto"
        cycle_dependent.save()
        self.assertEqual(cycle_dependent.cycle.id, Cycle.objects.get_active().id)

    def test_save_existing_cycle_dependent_doesnt_change_cycle(self):
        create_5_cycles_batch()
        first_cycle = Cycle.objects.first()
        # make sure first cycle is not the active one
        self.assertFalse(first_cycle.is_the_active_one)

        # create cycle_dependent with first cycle
        cycle_dependent = Company()
        cycle_dependent.cycle = first_cycle
        cycle_dependent.name = "toto"
        cycle_dependent.save()
        self.assertEqual(cycle_dependent.cycle.id, first_cycle.id)

        # change field in cycle_dependent doesn't change cycle
        cycle_dependent.refresh_from_db()
        cycle_dependent.name = "tutu"
        cycle_dependent.save()
        self.assertEqual(cycle_dependent.cycle.id, first_cycle.id)
