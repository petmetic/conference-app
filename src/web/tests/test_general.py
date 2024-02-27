from django.test import TestCase
from django.urls import reverse


class GeneralTest(TestCase):
    def test_index_page_loads(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text="Index page of Conference App")
