from django.test import TestCase

from kikeou.models.persons import Greeter
from tests.factories.persons import GreeterFactory

# FIXME: try to find a solution to have an independent model inheriting from abstract and script tests.
#        In the meantime, we use here Greeter model that inherit from PersonDependentAbstract.


class PersonDependentTestCase(TestCase):
    def test_person_dependent_str(self):
        self.assertEqual(
            str(GreeterFactory(person__first_name="Rose", person__last_name="")),
            "Rose",
        )

    def test_person_dependent_queryset_catch_related_person(self):
        GreeterFactory()
        person_dependent = Greeter.objects.get()
        with self.assertNumQueries(0):
            person_dependent.person.first_name
