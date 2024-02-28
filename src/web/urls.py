from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("atendee/list/", views.attendee_list, name="attendee_list"),
    path("atendee/<int:pk>/detail/", views.attendee, name="attendee"),
    path("atendee/<int:pk>/detail/edit/", views.attendee_edit, name="attendee_edit"),
    path("atendee/add/", views.attendee_add, name="attendee_add"),
    path("arrival/<int:pk>/detail/", views.arrival, name="arrival"),
    path("arrivals/check/", views.arrivals_check, name="arrivals_check"),
    path("arrivals/add/", views.arrivals_add, name="arrivals_add"),
]
