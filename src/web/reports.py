from datetime import datetime

from web.models import Attendee


def get_new_attendees():
    today = datetime.now()

    attendees = Attendee.objects.filter(added=today)
    print(type(attendees))
    print(attendees)

    return attendees


def get_new_arrivals(): ...
