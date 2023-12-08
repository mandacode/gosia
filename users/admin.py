from django.contrib import admin

from .models import UserProfile, BankAccount, Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'city', 'country',)

    def street_address(self, obj):
        return obj.street_address

    def city(self, obj):
        return obj.city

    def country(self, obj):
        return obj.country


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('bank_name',)
