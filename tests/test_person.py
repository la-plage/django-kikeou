from django.test import TestCase

from kikeou.models import Cycle, Person
from tests.utils.cycle import create_5_cycles_batch


class PersonTestCase(TestCase):
    def test_create_person_assigns_active_cycle_as_default(self):
        create_5_cycles_batch()
        self.assertEqual(
            Person.objects.create(first_name="toto").cycle.id,
            Cycle.objects.get_active().id,
        )

    def test_save_new_person_assigns_active_cycle_as_default(self):
        create_5_cycles_batch()
        person = Person()
        person.first_name = "toto"
        person.save()
        self.assertEqual(person.cycle.id, Cycle.objects.get_active().id)

    def test_save_existing_person_doesnt_change_cycle(self):
        create_5_cycles_batch()
        first_cycle = Cycle.objects.first()
        # make sure first cycle is not the active one
        self.assertFalse(first_cycle.is_the_active_one)

        # create person with first cycle
        person = Person()
        person.cycle = first_cycle
        person.first_name = "toto"
        person.save()
        self.assertEqual(person.cycle.id, first_cycle.id)

        # change field in person doesn't change cycle
        person.refresh_from_db()
        person.last_name = "tutu"
        person.save()
        self.assertEqual(person.cycle.id, first_cycle.id)
