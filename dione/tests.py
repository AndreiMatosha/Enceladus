import json
from django.test import TestCase
from django.test import Client

from dione.models import Company
from django.urls import reverse


class BasicCompanyApiTestCate(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.companies_url = reverse("companies")

    def tearDown(self) -> None:
        pass


# Create your tests here.
class TestNewCompany(BasicCompanyApiTestCate):
    def test_zero_companies_should_return_empty_list(self) -> None:
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)

    def test_get_one_existed_company_should_succeed(self):
        pass
