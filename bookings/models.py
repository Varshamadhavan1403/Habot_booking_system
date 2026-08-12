from django.db import models


# Create your models here.
class Parent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LSAProfile(models.Model):
    SKILL_CHOICES = [
        ("Autism", "Autism"),
        ("ADHD", "ADHD"),
        ("Dyslexia", "Dyslexia"),
        ("Speech Therapy", "Speech Therapy"),
        ("Behavioral Support", "Behavioral Support"),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    skill = models.CharField(max_length=50, choices=SKILL_CHOICES)
    experience_years = models.PositiveIntegerField(default=0)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.skill}"


class BookingRequest(models.Model):
    parent = models.ForeignKey(
        Parent, on_delete=models.CASCADE, related_name="bookings"
    )
    lsa = models.ForeignKey(
        LSAProfile, on_delete=models.CASCADE, related_name="bookings"
    )
    session_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("CANCELLED", "Cancelled"),
        ("FAILED", "Failed"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["lsa"]),
            models.Index(fields=["session_date"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return f"Booking #{self.id}"


class Payment(models.Model):
    booking = models.OneToOneField(
        BookingRequest, on_delete=models.CASCADE, related_name="payment"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    PAYMENT_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    ]
    payment_status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS_CHOICES, default="PENDING"
    )
    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id
