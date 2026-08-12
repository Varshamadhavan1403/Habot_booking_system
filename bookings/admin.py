from django.contrib import admin
from .models import BookingRequest, LSAProfile, Parent, Payment

# Register your models here.

admin.site.register(BookingRequest)
admin.site.register(LSAProfile)
admin.site.register(Parent)
admin.site.register(Payment)
