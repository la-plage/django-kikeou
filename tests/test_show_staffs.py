from django.test import TestCase

from tests.factories.show_staffs import ShowStaffFunctionFactory, ShowStaffMemberFactory


class ShowStaffFunctionTestCase(TestCase):
    def test_instance_str(self):
        self.assertEqual(
            str(ShowStaffFunctionFactory(name="Actress")),
            "Actress",
        )


class ShowStaffMemberTestCase(TestCase):
    def test_instance_str(self):
        self.assertEqual(
            str(
                ShowStaffMemberFactory(
                    person__first_name="Goldorak", person__last_name=""
                )
            ),
            "Goldorak",
        )
