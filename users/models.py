from django.db import models
from django.contrib.auth.models import User, AbstractUser


 # TODO kto jest uzytkownikiem? Mama
 # do czego ma sluzyc aplikacje? Do generowania rachunkow, jedynym uzytkownikiem jest mama, reszta to syntetyczne encje
    # jakie dane ma miec uzytkownik? Imie, nazwisko, adres, telefon, email, nip, bank account,
    # logowanie za pomoca emaila
    # use default django login features, no need for register, just create superuser malgorzatajarmul, same in heroku, invoice data will be added manually in admin panel

    # customer and employer are not users, they are just entities, they are not gonna USE the application, they are just added to the database by the admin,
class Address(models.Model):

    zip_code = models.CharField(max_length=6)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Address: {self.street_address}, {self.city}, {self.country}"


class BankAccount(models.Model):

    bank_name = models.CharField(max_length=255)
    iban = models.CharField(max_length=255)
    bic = models.CharField(max_length=255)

    def __str__(self):
        return f"BankAccount: {self.bank_name}"


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    phone_number = models.CharField(max_length=100)
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    bank_account = models.ForeignKey(
        BankAccount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    ust_idnr = models.CharField(max_length=100)
    nip = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"UserProfile: {self.user.first_name} {self.user.last_name}"
