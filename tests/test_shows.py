from django.test import TestCase

from tests.factories.shows import ShowFactory, ShowTypeFactory


class ShowTypeTestCase(TestCase):
    def test_instance_str(self):
        self.assertEqual(
            str(ShowTypeFactory(name="Fixed show")),
            "Fixed show",
        )


class ShowTestCase(TestCase):
    def test_instance_str_without_code(self):
        self.assertEqual(
            str(ShowFactory(name="MyShow", code="")),
            "MyShow",
        )

    def test_instance_str_with_code(self):
        self.assertEqual(
            str(ShowFactory(name="MyShow", code="666")),
            "[666] MyShow",
        )
