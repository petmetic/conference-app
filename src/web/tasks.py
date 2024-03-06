from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string


@shared_task
def send_daily_email_task():
    from .reports import get_new_attendees, get_new_attendee_count

    subject = "Conference App Report"
    html = render_to_string(
        "web/report.html",
        {
            "attendee_list": get_new_attendees(),
            "attendee_count": get_new_attendee_count(get_new_attendees()),
        },
    )
    from_email = "admin@conferenceapp.com"

    recipient_list = ["admin@conferenceapp.com"]
    send_mail(
        subject=subject,
        message=html,
        from_email=from_email,
        recipient_list=recipient_list,
    )

    return None
