import logging
import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BookingRequest, Parent, LSAProfile, Payment
from .serializers import (
    BookingRequestSerializer,
    ParentSerializer,
    LSAProfileSerializer,
)

# Create your views here.
logger = logging.getLogger(__name__)


class ParentCreateAPIView(APIView):

    def post(self, request):

        serializer = ParentSerializer(data=request.data)

        if serializer.is_valid():
            parent = serializer.save()

            return Response(
                {
                    "message": "Parent created successfully",
                    "data": ParentSerializer(parent).data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        parents = Parent.objects.all()

        serializer = ParentSerializer(parents, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


from .models import LSAProfile
from .serializers import LSAProfileSerializer


class LSACreateAPIView(APIView):

    def post(self, request):

        serializer = LSAProfileSerializer(data=request.data)

        if serializer.is_valid():
            lsa = serializer.save()

            return Response(
                {
                    "message": "LSA created successfully",
                    "data": LSAProfileSerializer(lsa).data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        lsas = LSAProfile.objects.all()

        serializer = LSAProfileSerializer(lsas, many=True)

        return Response(serializer.data)


class BookingCreateAPIView(APIView):
    def post(self, request):
        serializer = BookingRequestSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save()
            Payment.objects.create(
                booking=booking,
                amount=500.0,
                transaction_id=f"TXN-{booking.id}",
                payment_status="PENDING",
            )

            return Response(
                {
                    "message": "Booking created successfully",
                    "booking_id": booking.id,
                    "status": booking.status,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LSASearchAPIView(APIView):

    def get(self, request):

        skill = request.GET.get("skill")

        queryset = LSAProfile.objects.prefetch_related("bookings").filter(
            is_active=True
        )

        if skill:
            queryset = queryset.filter(skill__icontains=skill)

        serializer = LSAProfileSerializer(queryset, many=True)

        return Response(serializer.data)


class PaymentWebhookAPIView(APIView):

    def post(self, request):

        booking_id = request.data.get("booking_id")
        payment_status = request.data.get("status")

        try:
            booking = BookingRequest.objects.get(id=booking_id)

            payment = Payment.objects.get(booking=booking)

            payment.payment_status = payment_status
            payment.save()

            if payment_status == "SUCCESS":
                booking.status = "CONFIRMED"
            else:
                booking.status = "FAILED"

            booking.save()

            return Response(
                {"message": "Webhook processed successfully"}, status=status.HTTP_200_OK
            )

        except BookingRequest.DoesNotExist:
            return Response(
                {"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND
            )


class MockPaymentGatewayAPIView(APIView):

    def get(self, request):

        try:
            response = requests.get(
                "https://jsonplaceholder.typicode.com/posts/1", timeout=5
            )

            response.raise_for_status()

            return Response(response.json(), status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:

            logger.error(f"Payment Gateway Error: {str(e)}")

            return Response(
                {"error": "External service unavailable"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
