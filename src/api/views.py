from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .serializers import UserSerializer, AttendeeSerializer, ArrivalSerializer
from web.models import Attendee, Arrival


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AttendeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows attendee list to be viewed or edited.
    """

    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArrivalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows arrival list to be viewed or edited.
    """

    queryset = Arrival.objects.all()
    serializer_class = ArrivalSerializer
    permission_classes = [permissions.IsAuthenticated]
