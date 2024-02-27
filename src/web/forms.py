from django.forms import ModelForm

from django import forms
from django.core.exceptions import ValidationError

from .models import Attendee, Arrival


class AttendeeEditForm(ModelForm):
    name = forms.CharField(
        label="Name",
        label_suffix="",
        widget=forms.TextInput(attrs={"class": "form-control", "type": "text"}),
    )
    surname = forms.CharField(
        label="Surname",
        label_suffix="",
        widget=forms.TextInput(attrs={"class": "form-control", "type": "text"}),
    )
    birth_date = forms.DateField(
        label="Date of Birth",
        label_suffix="",
        widget=forms.DateTimeInput(
            format="%Y-%m-%d",
            attrs={"class": "form-control", "type": "date-local"},
        ),
    )
    ticket_id = forms.CharField(
        label="Ticket ID",
        label_suffix="",
        widget=forms.TextInput(attrs={"class": "form-control", "type": "text"}),
    )

    class Meta:
        model = Attendee
        fields = ["name", "surname", "birth_date", "ticket_id"]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data["name"]
        surname = cleaned_data["surname"]
        birth_date = cleaned_data["birth_date"]
        ticket_id = cleaned_data["ticket_id"]
        attendee = Attendee.objects.filter(
            name=name, surname=surname, birth_date=birth_date, ticket_id=ticket_id
        ).first()
        if attendee:
            raise ValidationError(
                "Customer already exists in database. Please check for correct input in fields."
            )
        return cleaned_data
