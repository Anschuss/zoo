from celery import shared_task
from .models import MessageInformation


@shared_task
def save_user_message(email, subject, text):
    message = MessageInformation(email=email, subject=subject, text=text)
    message.save()
