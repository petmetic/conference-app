from datetime import datetime
from django.test import TestCase
from django.urls import reverse
import pytz

from .factories import UserFactory, AttendeeFactory, ArrivalFactory

tz = pytz.timezone("Europe/Ljubljana")


class AttendeeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        The user (Alice) should see the attendee listing for Judy and Sean.
        """

        cls.user = UserFactory(
            username="alicejohnson", first_name="Alice", last_name="Johnson"
        )

        cls.attendeeJudy = AttendeeFactory(
            name="Judy", surname="Dench", ticket_id="thisisanexampleticket1234"
        )
        cls.attendeeSean = AttendeeFactory(
            name="Sean", surname="Connery", ticket_id="thisisanexampleticket5678"
        )

        cls.arrivalJudy = ArrivalFactory(
            attendee=cls.attendeeJudy,
            arrival=datetime(2023, 8, 1, 18, 0, 0).astimezone(tz=tz),
        )
        cls.arrivalSean = ArrivalFactory(
            attendee=cls.attendeeSean,
            arrival=datetime(2023, 8, 2, 18, 0, 0).astimezone(tz=tz),
        )

    def test_attendee_list_page_displays(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("attendee_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text="List of Attendees")
