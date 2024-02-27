from django.contrib import admin
from .models import Attendee, Arrival


@admin.register(Arrival)
class ArrivalAdmin(admin.ModelAdmin):
    list_filter = ["arrival"]
    list_display = ["arrival", "attendee"]


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_filter = ["ticket_id"]
    list_display = ["name", "surname", "birth_date", "ticket_id"]
