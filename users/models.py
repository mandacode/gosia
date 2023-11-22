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


class CustomerProfile(models.Model):

    hourly_rate = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=15
    )


class EmployeeProfile(models.Model):

    nip = models.CharField(max_length=10)


class BankAccount(models.Model):

    bank_name = models.CharField(max_length=255)
    iban = models.CharField(max_length=255)
    bic = models.CharField(max_length=255)


class OwnerProfile(models.Model):

    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    ust_idnr = models.CharField(max_length=100)
    nip = models.CharField(max_length=10)
    bank_account = models.OneToOneField(
        BankAccount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
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
    owner_profile = models.OneToOneField(
        OwnerProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='owner_profile'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
