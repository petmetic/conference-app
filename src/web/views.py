from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login

from .forms import (
    AttendeeEditForm,
    AttendeeForm,
    ArrivalForm,
    CustomAuthenticationForm,
    SignUpForm,
)
from .models import Attendee, Arrival


def index(request):
    return render(request, "web/index.html", {})


@login_required
def attendee_add(request):
    if request.method == "POST":
        form = AttendeeForm(request.POST)
        if form.is_valid():
            attendee = form.save()

            return redirect(reverse("attendee", kwargs={"pk": attendee.pk}))

    else:
        form = AttendeeForm()
    return render(request, "web/attendee_add.html", {"form": form})


@login_required
def attendee(request, pk: int):
    attendee = get_object_or_404(Attendee, pk=pk)
    return render(request, "web/attendee.html", {"attendee": attendee})


@login_required
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


@login_required
def attendee_list(request):
    attendees = Attendee.objects.all().order_by("surname")
    return render(request, "web/attendee_list.html", {"attendee_list": attendees})


@login_required
def arrivals_check(request):
    arrivals = Arrival.objects.filter()
    return render(
        request,
        "web/arrivals_check.html",
        {"arrival_list": arrivals},
    )


@login_required
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


@login_required
def arrival(request, pk: int):
    arrival = get_object_or_404(Arrival, pk=pk)
    return render(request, "web/arrival.html", {"arrival": arrival})


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


def custom_logout(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, "registration/register.html", {"form": form})
