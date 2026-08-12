# HabotConnect LSA Booking System

## Overview

HabotConnect LSA Booking System is a Django REST Framework based backend application that enables parents to book Learning Support Assistants (LSAs) for specialized educational support sessions.

The system provides APIs for managing parents, LSAs, bookings, payment processing, and external service integration while ensuring booking conflict validation and automated testing.

---

## Features

- Parent Management API
- LSA Profile Management API
- LSA Search API
- Booking Management API
- Booking Conflict Detection
- Payment Gateway Integration
- Payment Webhook Processing
- PostgreSQL Database Support
- Automated Unit Testing
- CI/CD using GitHub Actions

---

## Tech Stack

- Python 3.12+
- Django
- Django REST Framework (DRF)
- PostgreSQL
- SQLite (for CI testing)
- Requests
- GitHub Actions

---

## Database Models

### Parent
Stores parent information.

### LSAProfile
Stores Learning Support Assistant details including skills and experience.

### BookingRequest
Manages booking requests between parents and LSAs.

### Payment
Tracks payment status for bookings.

---

## API Endpoints

### Parent APIs

```http
POST /api/v1/parents/
```

### LSA APIs

```http
POST /api/v1/lsas/
GET /api/v1/lsas/search/
```

### Booking APIs

```http
POST /api/v1/bookings/
```

### Payment APIs

```http
GET /api/payment-gateway/
POST /api/payments/webhook/
```

---

## Query Optimization

To improve performance and avoid N+1 query issues:

- select_related()
- prefetch_related()
- Database indexing

---

## Environment Setup

Copy `.env.example` to `.env` and update the values.

```bash
cp .env.example .env
```

Windows users can create `.env` manually and copy the contents from `.env.example`.

## Environment Variables

Create a `.env` file in the project root based on the following template:

```env
SECRET_KEY=your-secret-key

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Habot_booking_system
```

Create a virtual environment:

```bash
python -m venv bookingenv
```

Activate the virtual environment:

### Windows

```bash
bookingenv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

---

## Running Tests

Execute all tests using:

```bash
python manage.py test
```

---

## CI/CD

GitHub Actions is configured to automatically:

- Install project dependencies
- Run Django test cases
- Validate the application on every push and pull request

---

## Test Coverage

The project includes automated tests for:

- Parent Creation API
- LSA Creation API
- LSA Search API
- Booking Creation API
- Booking Conflict Validation
- Payment Webhook API
- Invalid Booking Scenarios

---

## Author

**Varsha Madhavan**

Python Developer | Django & Django REST Framework