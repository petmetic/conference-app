from django.test import TestCase
from django.urls import reverse


from .factories import UserFactory, AttendeeFactory, ArrivalFactory


class GeneralTest(TestCase):
    def test_index_page_loads(self):
        user = UserFactory()
        self.client.force_login(user)
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text="Welcome to the Conference APP")
