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

        expected_data_from_api = {
            "attendee": f"http://testserver/api/attendee/{arrival.attendee.id}/",
            "arrival": "2023-08-02T16:00:00Z",
        }

        resp = self.client.post(self.url_arrival, data=data)
        self.assertEqual(resp.status_code, 201)

        returned_data_from_resp = resp.json()

        # is response data from POST request == expected data
        self.assertEqual(returned_data_from_resp, expected_data_from_api)

        # has arrival from API been written in db
        arrival_in_db = Arrival.objects.latest("id")

        arrival_time = arrival_in_db.arrival.strftime("%Y-%m-%dT%H:%M:%SZ")

        self.assertEqual(returned_data_from_resp["arrival"], arrival_time)
