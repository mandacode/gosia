from django.db import models
from django.contrib.auth.models import User


class UserType(models.TextChoices):
    CUSTOMER = 'customer'
    EMPLOYEE = 'employee'
    OWNER = 'owner'


class Address(models.Model):
    zip_code = models.CharField(max_length=6)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Address: {self.street_address}, {self.city}, {self.country}>"

    def __str__(self):
        return f"<Address: {self.street_address}, {self.city}, {self.country}>"

class BankAccount(models.Model):

    bank_name = models.CharField(max_length=255)
    iban = models.CharField(max_length=255)
    bic = models.CharField(max_length=255)


class OwnerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='owner_profile'
    )
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    ust_idnr = models.CharField(max_length=100)
    nip = models.CharField(max_length=10)
    bank_account = models.OneToOneField(
        BankAccount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='owner_profile'
    )


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
    type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.EMPLOYEE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerProfile(models.Model):
    hourly_rate = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=15
    )
    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='customer_profile'
    )


class EmployeeProfile(models.Model):
    nip = models.CharField(max_length=10)
    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='employee_profile'
    )
