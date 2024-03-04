import json
from datetime import datetime
import pytz

from django.urls import reverse
from rest_framework.test import APITestCase

from web.models import Arrival
from web.tests.factories import UserFactory, AttendeeFactory, ArrivalFactory


class TestAttendeeAPIView(APITestCase):
    def setUp(self):
        self.url_attendee = reverse("attendee-list")
        self.url_arrival = reverse("arrivals_add")
        self.user = UserFactory()
        self.attendee = AttendeeFactory()
        self.client.force_login(self.user)

    def test_get_attendees(self):
        response = self.client.get(self.url_attendee)
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
        ticket_id_api = response_data[0]["ticket_id"]

        name_expected = expected_content["name"]
        name_api = response_data[0]["name"]

        self.assertEqual(ticket_id_expected, ticket_id_api)
        self.assertEqual(name_expected, name_api)


class TestArrivalAPIView(APITestCase):
    def setUp(self):
        self.url_arrival = reverse("arrival-list")
        self.user = UserFactory()
        self.attendee = AttendeeFactory(name="Christine")
        self.client.force_login(self.user)

    def test_post_arrival(self):

        arrival = ArrivalFactory.build(
            attendee=self.attendee,
            arrival=datetime(2023, 8, 2, 16, 0, 0, tzinfo=pytz.UTC),
        )

        data = {
            "attendee": f"http://127.0.0.1:8000/api/attendee/{arrival.attendee.id}/",
            "arrival": arrival.arrival.strftime("%Y-%m-%d %H:%M:%S%z"),
        }

        expected_data = {
            "attendee": f"http://testserver/api/attendee/{arrival.attendee.id}/",
            "arrival": "2023-08-02 16:00:00+0000",
        }

        resp = self.client.post(self.url_arrival, data=data)
        self.assertEqual(resp.status_code, 201)

        returned_data = resp.content

        self.assertEqual(returned_data, expected_data)

        arrival = Arrival.objects.latest("id")

        arrival_time = arrival.arrival.strftime("%Y-%m-%d %H:%M:%S%z")

        self.assertEqual(expected_data["arrival"], arrival_time)
        self.assertEqual(expected_data["arrival"], arrival_time)
