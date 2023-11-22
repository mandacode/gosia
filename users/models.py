from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    zip_code = models.CharField(max_length=6)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Address: {self.street_address}, {self.city}, {self.country}>"


class CustomerProfile(models.Model):

    hourly_rate = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=15
    )


class EmployeeProfile(models.Model):

    nip = models.CharField(max_length=10)


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_customer = models.BooleanField(default=False)
    customer_profile = models.OneToOneField(
        CustomerProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='customer_profile'
    )
    employee_profile = models.OneToOneField(
        EmployeeProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employee_profile'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
