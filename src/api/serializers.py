from django.contrib.auth.models import User
from rest_framework import serializers

from web.models import Attendee, Arrival


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email"]


class AttendeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendee
        fields = ["name", "surname", "birth_date", "ticket_id"]


class ArrivalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arrival
        fields = ["attendee", "arrival"]
