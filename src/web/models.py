from django.db import models

from simple_history.models import HistoricalRecords


class Arrival(models.Model):
    attendee = models.ForeignKey("Attendee", on_delete=models.CASCADE)
    arrival = models.DateTimeField(blank=True, null=True)

    added = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.arrival}, {self.attendee}"


class Attendee(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, null=True, default="")
    birth_date = models.DateField(blank=True, null=True)
    ticket_id = models.CharField(max_length=200, null=True, default="")

    added = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name} {self.surname}"
