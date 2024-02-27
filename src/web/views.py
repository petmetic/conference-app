from django.shortcuts import render, get_object_or_404

from .models import Attendee


def index(request):
    return render(request, "web/index.html", {})


def attendee_add(request):
    return render(request, "web/attendee_add.html", {})


def attendee(request, pk: int):
    attendee = get_object_or_404(Attendee, pk=pk)
    return render(request, "web/attendee.html", {"attendee": attendee})


def attendee_edit(request, pk: int):
    attendee = get_object_or_404(Attendee, pk=pk)

    return render(request, "web/attendee_edit.html", {"attendee": attendee})


def attendee_list(request):
    attendees = Attendee.objects.all().order_by("surname")
    return render(request, "web/attendee_list.html", {"attendee_list": attendees})


def arrivals_check(request):
    return render(request, "web/arrivals_check.html", {})


def arrivals_add(request):
    return render(request, "web/arrivals_add.html", {})
