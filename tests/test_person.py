from django.test import TestCase

from kikeou.models.person import Greeter, LocationContact, Programmer, StageManager
from tests.factories.cycle import CycleFactory
from tests.factories.person import PersonFactory


class PersonTestCase(TestCase):
    def test_full_name_build(self):
        self.assertEqual(
            PersonFactory(first_name="Georges", last_name="Dupont").full_name,
            "Georges Dupont",
        )

    def test_person_str_is_full_name(self):
        person = PersonFactory(first_name="Georges", last_name="Dupont")
        self.assertEqual(
            str(person),
            person.full_name,
        )


class GreeterTestCase(TestCase):
    def test_queryset_exclude_non_greeter_persons(self):
        PersonFactory()
        greeter = PersonFactory(is_greeter=True)
        self.assertEqual(Greeter.objects.get().id, greeter.id)

    def test_save_greeter_instance_set_is_greeter_true(self):
        CycleFactory()
        greeter = Greeter()
        greeter.first_name = "toto"
        greeter.save()
        self.assertEqual(Greeter.objects.count(), 1)


class LocationContactTestCase(TestCase):
    def test_queryset_exclude_non_location_contact_persons(self):
        PersonFactory()
        location_contact = PersonFactory(is_location_contact=True)
        self.assertEqual(LocationContact.objects.get().id, location_contact.id)

    def test_save_location_contact_instance_set_is_greeter_true(self):
        CycleFactory()
        location_contact = LocationContact()
        location_contact.first_name = "toto"
        location_contact.save()
        self.assertEqual(LocationContact.objects.count(), 1)


class ProgrammerTestCase(TestCase):
    def test_queryset_exclude_non_programmer_persons(self):
        PersonFactory()
        programmer = PersonFactory(is_programmer=True)
        self.assertEqual(Programmer.objects.get().id, programmer.id)

    def test_save_programmer_instance_set_is_greeter_true(self):
        CycleFactory()
        programmer = Programmer()
        programmer.first_name = "toto"
        programmer.save()
        self.assertEqual(Programmer.objects.count(), 1)


class StageManagerTestCase(TestCase):
    def test_queryset_exclude_non_stage_manager_persons(self):
        PersonFactory()
        stage_manager = PersonFactory(is_stage_manager=True)
        self.assertEqual(StageManager.objects.get().id, stage_manager.id)

    def test_save_stage_manager_instance_set_is_greeter_true(self):
        CycleFactory()
        stage_manager = StageManager()
        stage_manager.first_name = "toto"
        stage_manager.save()
        self.assertEqual(StageManager.objects.count(), 1)
