from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("accounts/login/", views.CustomLoginView.as_view(), name="login"),
    path("attendee/list/", views.attendee_list, name="attendee_list"),
    path("attendee/<int:pk>/detail/", views.attendee, name="attendee"),
    path("attendee/<int:pk>/detail/edit/", views.attendee_edit, name="attendee_edit"),
    path("attendee/add/", views.attendee_add, name="attendee_add"),
    path("arrival/<int:pk>/detail/", views.arrival, name="arrival"),
    path("arrivals/check/", views.arrivals_check, name="arrivals_check"),
    path("arrivals/add/", views.arrivals_add, name="arrivals_add"),
    path("logout/", views.custom_logout, name="logout"),
    path("", views.index, name="index"),
]
