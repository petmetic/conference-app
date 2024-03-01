from django.contrib import admin
from .models import Attendee, Arrival
from simple_history.admin import SimpleHistoryAdmin


@admin.register(Arrival)
class ArrivalAdmin(SimpleHistoryAdmin):
    list_filter = ["arrival"]
    list_display = ["arrival", "attendee"]


@admin.register(Attendee)
class AttendeeAdmin(SimpleHistoryAdmin):
    list_filter = ["ticket_id"]
    list_display = ["name", "surname", "birth_date", "ticket_id"]
