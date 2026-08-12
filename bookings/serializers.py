from rest_framework import serializers
from bookings.models import BookingRequest, Parent, LSAProfile, Payment


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"


class LSAProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LSAProfile
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class BookingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingRequest
        fields = "__all__"

    def validate(self, data):
        start_time = data["start_time"]
        end_time = data["end_time"]
        lsa = data["lsa"]

        if end_time <= start_time:
            raise serializers.ValidationError("End time must be after start time.")

        overlapping_booking = BookingRequest.objects.filter(
            lsa=lsa,
            start_time__lt=end_time,
            end_time__gt=start_time,
            status__in=["PENDING", "CONFIRMED"],
        ).exists()

        if overlapping_booking:
            raise serializers.ValidationError(
                "The selected LSA is already booked for the specified time slot."
            )

        return data
