from django.test import TestCase

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
