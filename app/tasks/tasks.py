from pydantic import EmailStr
from celery import shared_task
import smtplib

from app.tasks.celery import celery
from app.email_templates import tanks_for_registrating_template
from app.config import settings



@celery.task
def add(x, y):
    return f"\nВсе работает {x + y}"


# add.delay(10, 20)


@shared_task
def send_email(receiver: EmailStr):
    msg_content = tanks_for_registrating_template(receiver)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)