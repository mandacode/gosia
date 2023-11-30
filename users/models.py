from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.TextChoices):

    CUSTOMER = 'customer'
    EMPLOYEE = 'employee'
    ADMIN = 'admin'


class User(AbstractUser):

    username = models.CharField(max_length=255, unique=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):

    zip_code = models.CharField(max_length=6)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
        default=UserType.EMPLOYEE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<UserProfile: {self.user.first_name} {self.user.last_name}>"


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

    def __str__(self):
        return f"<CustomerProfile: {self.user_profile.user.first_name} {self.user_profile.user.last_name}>"


class EmployeeProfile(models.Model):

    nip = models.CharField(max_length=10, null=True, blank=True)
    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='employee_profile'
    )

    def __str__(self):
        return f"<EmployeeProfile: {self.user_profile.user.first_name} {self.user_profile.user.last_name}>"
