from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("atendee/add", views.attendee_add, name="attendee_add"),
    path("atendee/list", views.attendee_list, name="attendee_list"),
    path("arrivals/check", views.arrivals_check, name="arrivals_check"),
    path("arrivals/add", views.arrivals_add, name="arrivals_add"),
]
