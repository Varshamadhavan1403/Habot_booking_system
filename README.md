\# HabotConnect LSA Booking System



\## Overview



Backend system developed using Django REST Framework for managing Learning Support Assistant (LSA) bookings.



\## Features



\- Parent Management

\- LSA Profile Management

\- Booking API

\- Payment Webhook

\- External Service Integration

\- Automated Tests

\- CI/CD with GitHub Actions



\## Tech Stack



\- Python

\- Django

\- DRF

\- PostgreSQL

\- Requests

\- Pytest



\## Database Design



Parent

|

BookingRequest

|

LSAProfile



BookingRequest

|

Payment



\## API Endpoints



POST /api/v1/bookings/



GET /api/v1/lsas/search/



POST /api/payments/webhook/



GET /api/payment-gateway/



\## Query Optimization



Used:



\- prefetch\_related()

\- database indexes



to avoid N+1 query problems.



\## Running Project



pip install -r requirements.txt



python manage.py migrate



python manage.py runserver



\## Running Tests



python manage.py test

