# customers/tasks.py
from celery import shared_task
from .models import Customer
from django.core.mail import send_mail
from datetime import date

@shared_task
def send_birthday_emails():
    today = date.today()
    customers = Customer.objects.filter(birthday__day=today.day, birthday__month=today.month)
    for customer in customers:
        send_mail(
            'Happy Birthday!',
            f'Hi {customer.name},\n\nHappy birthday! We hope you have a fantastic day!',
            'your@email.com',
            [customer.email],
            fail_silently=False,
        )
