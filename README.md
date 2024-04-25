# Birthday Wishing Through Email

This Django project automates birthday wishes by sending emails to customers on their birthdays. It provides a RESTful API for customer registration and integrates Celery with Django for handling background tasks, such as sending birthday emails.

## Features

- Register customers with their name, email, and birthday using a RESTful API endpoint.
- Automatically send birthday emails to customers on their birthdays.
- Celery task scheduler ensures timely delivery of birthday emails.
- Simulated email sending process for testing purposes.

## Technologies Used

- Django: Web framework for building the backend API.
- Django Rest Framework (DRF): Toolkit for building RESTful APIs in Django.
- Celery: Distributed task queue for executing asynchronous tasks.
- Redis: Message broker used by Celery for task coordination.
- Python: Programming language used for backend development.
- Postman: API development and testing tool for testing API endpoints.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/birthday-wishing.git

2. Install dependencies:

   ```bash
   cd birthday-wishing
   python3 -m venv env
   source env/bin/activate. Use this command if you're using Ubuntu/WSL2
   pip install -r requirements.txt

3. Configure Redis:
   
   Install and configure Redis as the message broker for Celery.

4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate


5. Start Redis server:

   ```bash
   redis-server

6. Start Celery worker:

   ```bash
   celery -A birthday_wishing worker --loglevel=info

7. Start Celery beat:

   ```bash
   celery -A birthday_wishing beat --loglevel=info

8. Run the migration server:

   ```bash
   python manage.py runserver

9. (Optional) Create a superuser

   ```bash
   python manage.py createsuperuser

## API Endpoints

## API Endpoints

- `/customer/register/`: POST endpoint for registering a new customer with name, email, and birthday.
- `/customer/<int:pk>/`: POST endpoint for retrieving a customer by their primary key.

## Testing

- Use Postman or cURL to test the API endpoints.
- Test Celery tasks by triggering them manually or inspecting Celery logs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

