from datetime import date

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import AttendeeEditForm, AttendeeForm, ArrivalForm
from .models import Attendee, Arrival


def index(request):
    return render(request, "web/index.html", {})


def attendee_add(request):
    if request.method == "POST":
        form = AttendeeForm(request.POST)
        if form.is_valid():
            attendee = form.save()
            return redirect(reverse("attendee", kwargs={"pk": attendee.pk}))

    else:
        form = AttendeeForm()
    return render(request, "web/attendee_add.html", {"form": form})


def attendee(request, pk: int):
    attendee = get_object_or_404(Attendee, pk=pk)
    return render(request, "web/attendee.html", {"attendee": attendee})


def attendee_edit(request, pk: int):
    attendee = get_object_or_404(Attendee, pk=pk)

    if request.method == "POST":
        form = AttendeeEditForm(
            request.POST,
            instance=attendee,
            initial={"attendee": attendee},
        )
        if form.is_valid():
            attendee = form.save()
            return redirect(reverse("attendee", kwargs={"pk": attendee.pk}))
    else:
        form = AttendeeEditForm(instance=attendee, initial={"attendee": attendee})

    return render(
        request, "web/attendee_edit.html", {"form": form, "attendee": attendee}
    )


def attendee_list(request):
    attendees = Attendee.objects.all().order_by("surname")
    return render(request, "web/attendee_list.html", {"attendee_list": attendees})


def arrivals_check(request):
    arrivals = Arrival.objects.all()
    return render(request, "web/arrivals_check.html", {"arrival_list": arrivals})


def arrivals_add(request):
    if request.method == "POST":
        form = ArrivalForm(request.POST)
        if form.is_valid():
            arrival = form.save()
            return redirect(reverse("arrival", kwargs={"pk": arrival.pk}))
    else:
        form = ArrivalForm()

    return render(
        request,
        "web/arrivals_add.html",
        {"form": form},
    )


def arrival(request, pk: int):
    arrival = get_object_or_404(Arrival, pk=pk)
    return render(request, "web/arrival.html", {"arrival": arrival})
