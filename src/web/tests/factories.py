import factory
from .. import models
import pytz
from django.contrib.auth.models import User

tz = pytz.timezone("Europe/Ljubljana")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "Agent %03d" % n)
    first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    last_name = factory.Sequence(lambda n: "Agent %03d" % n)
    email = factory.Sequence(lambda n: "Agent %03d" % n)
    password = factory.django.Password("pw")


class AttendeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Attendee

    name = factory.Faker("first_name")
    surname = factory.Faker("last_name")
    birth_date = factory.Faker("date_object")  # "%Y-%m-%d"
    ticket_id = factory.Faker("sentence")


class ArrivalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Arrival

    attendee = factory.SubFactory(AttendeeFactory)
    arrival = factory.Faker("date_time", tzinfo=tz)  # "%Y-%m-%d %H:%M:%S"
