from datetime import datetime

from web.models import Attendee


def get_new_attendees():
    today = datetime.now().date()
    new_attendees = Attendee.objects.filter(added__date=today).order_by("surname")

    return new_attendees


def get_new_attendee_count(new_attendees):
    attendee_count = 0
    for attendee in new_attendees:
        attendee_count += 1

    return attendee_count
