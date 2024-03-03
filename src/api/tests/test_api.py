import json
from django.urls import reverse
from rest_framework.test import APITestCase

from web.tests.factories import UserFactory, AttendeeFactory, ArrivalFactory


class TestAttendeeAPIView(APITestCase):
    def setUp(self):
        self.url = reverse("attendee-list")
        self.user = UserFactory()
        self.attendee = AttendeeFactory()
        self.arrival = ArrivalFactory()
        self.client.force_login(self.user)

    def test_get_attendees(self):
        response = self.client.get(self.url)
        response.render()
        self.assertEquals(response.status_code, 200)

        expected_content = {
            "name": self.attendee.name,
            "surname": self.attendee.surname,
            "birth_date": self.attendee.birth_date,
            "ticket_id": self.attendee.ticket_id,
        }

        response_data = json.loads(response.content)

        ticket_id_expected = expected_content["ticket_id"]
        ticket_id_api = response_data["ticket_id"]

        name_expected = expected_content["name"]
        name_api = response_data["name"]

        self.assertEqual(ticket_id_expected, ticket_id_api)
        self.assertEqual(name_expected, name_api)
