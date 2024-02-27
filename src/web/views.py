from django.shortcuts import render


def index(request):
    return render(request, "web/index.html", {})


def attendee_add(request):
    return render(request, "web/attendee_add.html", {})


def attendee_list(request):
    return render(request, "web/attendee_list.html", {})


def arrivals_check(request):
    return render(request, "web/arrivals_check.html", {})


def arrivals_add(request):
    return render(request, "web/arrivals_add.html", {})
