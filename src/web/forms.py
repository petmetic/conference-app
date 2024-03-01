from django.forms import ModelForm

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

from .models import Attendee, Arrival


class AttendeeForm(ModelForm):
    name = forms.CharField(
        label="Name",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "enter NAME of atendee",
            }
        ),
    )
    surname = forms.CharField(
        label="Surname",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "enter SURNAME of attendee",
            }
        ),
    )
    birth_date = forms.DateField(
        label="Date of Birth",
        label_suffix="",
        widget=forms.DateTimeInput(
            format="%Y-%m-%d",
            attrs={
                "class": "form-control fw-light",
                "type": "date",
            },
        ),
    )
    ticket_id = forms.CharField(
        label="Ticket ID",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "enter ID number of ticket",
            }
        ),
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


class ArrivalForm(ModelForm):

    def __init__(self, *args, **kwargs):

        super(ArrivalForm, self).__init__(*args, **kwargs)
        self.fields["attendee"].help_text = "Select attendee name bellow"

    attendee = forms.ModelChoiceField(
        queryset=Attendee.objects.all().order_by("surname"),
        label="Attendee",
        label_suffix="",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    arrival = forms.DateTimeField(
        label="Arrival Time",
        label_suffix="",
        widget=forms.DateTimeInput(
            format="%Y-%m-%d %H:%M:%S",
            attrs={"class": "form-control", "type": "datetime-local"},
        ),
    )

    class Meta:
        model = Arrival

        fields = ["attendee", "arrival"]


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {"placeholder": "Username", "class": "form-control"}
        )
        self.fields["password"].widget.attrs.update(
            {"placeholder": "Password", "class": "form-control"}
        )
