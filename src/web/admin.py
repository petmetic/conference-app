from django.contrib import admin
from .models import Attendee, Arrival
from simple_history.admin import SimpleHistoryAdmin


@admin.register(Arrival)
class ArrivalAdmin(SimpleHistoryAdmin):
    list_filter = ["arrival"]
    list_display = ["attendee", "arrival"]

    search_fields = [
        "attendee__name",
        "attendee__surname",
        "attendee__ticket_id",
        "arrival",
    ]
    search_help_text = "Search here using Name, Surname, Ticket ID or arrival date in following format: YYYY-MM-DD"


@admin.register(Attendee)
class AttendeeAdmin(SimpleHistoryAdmin):
    list_filter = ["ticket_id"]
    list_display = ["surname", "name", "birth_date", "ticket_id"]
    search_fields = ["surname", "name", "ticket_id"]
    search_help_text = "Search here using Name, Surname, or Ticket ID"
