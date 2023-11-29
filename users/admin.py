from django.contrib import admin

from .models import UserProfile, OwnerProfile, EmployeeProfile, CustomerProfile, BankAccount, Address




@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'type')


@admin.register(OwnerProfile)
class OwnerProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

    def user(self, obj):
        return obj.customer_profile.user.first_name + ' ' + obj.customer_profile.user.last_name


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

    def user(self, obj):
        return obj.customer_profile.user.first_name + ' ' + obj.customer_profile.user.last_name


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank_name',)

    def user(self, obj):
        user = obj.owner_profile.user
        return user.first_name + ' ' + user.last_name

