from django.test import TestCase

from tests.factories import CompanyFactory


class CompanyTestCase(TestCase):
    def test_company_str(self):
        company = CompanyFactory()
        self.assertEqual(
            str(company),
            company.name,
        )
