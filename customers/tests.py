from datetime import date
from unittest.mock import patch
from django.test import TestCase
from customers.models import Customer
from customers.tasks import send_birthday_emails


class SendBirthdayEmailsTestCase(TestCase):
    @patch('customers.tasks.send_mail')
    def test_send_birthday_emails(self, mock_send_mail):
        # Create a customer with today's birthday
        today = date.today()
        customer = Customer.objects.create(
            name='Test Customer',
            email='test@example.com',
            birthday=today
        )

        # Call the Celery task
        send_birthday_emails()

        # Check that send_mail was called with the correct arguments
        mock_send_mail.assert_called_once_with(
            'Happy Birthday!',
            f'Hi {customer.name},\n\nHappy birthday! We hope you have a fantastic day!',
            'your@email.com',
            [customer.email],
            fail_silently=False,
        )