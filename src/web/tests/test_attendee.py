from datetime import datetime
from django.test import TestCase
from django.urls import reverse
import pytz

from .factories import UserFactory, AttendeeFactory, ArrivalFactory
from ..models import Attendee

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
        cls.attendeeClark = AttendeeFactory.build(
            name="Clark", surname="Kent", ticket_id="thisisanexampleticket9101"
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
        self.assertContains(response, text="Judy")
        self.assertContains(response, text="Connery")

    def test_attendee_adds_on_submit(self):
        self.client.force_login(self.user)

        data = {
            "name": self.attendeeClark.name,
            "surname": self.attendeeClark.surname,
            "birth_date": self.attendeeClark.birth_date,
            "ticket_id": self.attendeeClark.ticket_id,
        }

        attendee_previous = Attendee.objects.latest("id")
        response = self.client.post(reverse("attendee_add"), data=data)

        attendee_new = Attendee.objects.latest("id")

        self.assertNotEqual(attendee_previous.id, attendee_new.id)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("attendee", kwargs={"pk": attendee_new.id})
        )

        response = self.client.get(response.url)
        self.assertContains(response, text="Clark")
