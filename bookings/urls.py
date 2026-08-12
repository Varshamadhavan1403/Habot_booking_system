from django.urls import path
from .views import (
    BookingCreateAPIView,
    LSASearchAPIView,
    PaymentWebhookAPIView,
    MockPaymentGatewayAPIView,
    ParentCreateAPIView,
    LSACreateAPIView,
)

urlpatterns = [
    path("api/v1/parents/", ParentCreateAPIView.as_view(), name="create-parent"),
    path("api/v1/lsas/", LSACreateAPIView.as_view(), name="create-lsa"),
    path("api/v1/bookings/", BookingCreateAPIView.as_view(), name="create-booking"),
    path("api/v1/lsas/search/", LSASearchAPIView.as_view(), name="lsa-search"),
    path(
        "api/payments/webhook/", PaymentWebhookAPIView.as_view(), name="payment-webhook"
    ),
    path(
        "api/payment-gateway/",
        MockPaymentGatewayAPIView.as_view(),
        name="mock-payment-gateway",
    ),
]
