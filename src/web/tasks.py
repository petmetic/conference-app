from celery import shared_task
from django.core.mail import send_mail
from .reports import get_user_id


@shared_task
def send_daily_email_task(user):
    user_id = get_user_id(user)

    subject = "Conference App Report"
    message = "These were the new arrivals today: [list of arrivals] \n The total amount of Arrivals: [count]"
    from_email = "admin@conferenceapp.com"

    # lookup user_id in db; put user_id in recipient list instead of request
    recipient_list = [user_id.user.email]
    send_mail(subject, message, from_email, recipient_list)

    return None
