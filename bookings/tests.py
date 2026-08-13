from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Parent, LSAProfile, BookingRequest


class BookingAPITest(APITestCase):

    def setUp(self):
        self.parent = Parent.objects.create(
            name="Varsha", email="varsha@gmail.com", phone_number="9876543210"
        )

        self.lsa = LSAProfile.objects.create(
            name="Anu",
            email="anu@gmail.com",
            skill="Autism",
            experience_years=5,
            hourly_rate=500,
        )

    def test_create_booking_success(self):

        payload = {
            "parent": self.parent.id,
            "lsa": self.lsa.id,
            "session_date": "2026-08-15",
            "start_time": "2026-08-15T10:00:00Z",
            "end_time": "2026-08-15T11:00:00Z",
            "notes": "Support needed",
        }

        response = self.client.post("/api/v1/bookings/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lsa_search(self):

        response = self.client.get("/api/v1/lsas/search/?skill=Autism")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_time_range(self):

        payload = {
            "parent": self.parent.id,
            "lsa": self.lsa.id,
            "session_date": "2026-08-15",
            "start_time": "2026-08-15T11:00:00Z",
            "end_time": "2026-08-15T10:00:00Z",
        }

        response = self.client.post("/api/v1/bookings/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_booking_rejected(self):

        BookingRequest.objects.create(
            parent=self.parent,
            lsa=self.lsa,
            session_date="2026-08-15",
            start_time="2026-08-15T10:00:00Z",
            end_time="2026-08-15T11:00:00Z",
        )

        payload = {
            "parent": self.parent.id,
            "lsa": self.lsa.id,
            "session_date": "2026-08-15",
            "start_time": "2026-08-15T10:30:00Z",
            "end_time": "2026-08-15T11:30:00Z",
        }

        response = self.client.post("/api/v1/bookings/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_webhook_invalid_booking(self):

        response = self.client.post(
            "/api/payments/webhook/",
            {"booking_id": 999, "status": "SUCCESS"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_parent(self):

        payload = {
            "name": "New Parent",
            "email": "newparent@gmail.com",
            "phone_number": "987654321",
        }

        response = self.client.post("/api/v1/parents/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_lsa(self):

        payload = {
            "name": "Anu",
            "email": "anu123@gmail.com",
            "skill": "Dyslexia",
            "experience_years": 5,
            "hourly_rate": "500.00",
            "is_active": True,
        }

        response = self.client.post("/api/v1/lsas/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
