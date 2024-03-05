from celery.worker import request


def get_user_id(user):
    if request.user.is_authenticated:
        user_id = request.user.id

    return user_id
