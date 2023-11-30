from django.contrib import admin

from .models import UserProfile, OwnerProfile, EmployeeProfile, CustomerProfile, BankAccount, User, Address
from .forms import UserForm


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
        return obj.user_profile.user.first_name + ' ' + obj.user_profile.user.last_name


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

    def user(self, obj):
        return obj.user_profile.user.first_name + ' ' + obj.user_profile.user.last_name


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank_name',)

    def user(self, obj):
        user = obj.owner_profile.user
        return user.first_name + ' ' + user.last_name


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm

    def save_form(self, request, form, change):

        user = super().save_form(request, form, change)
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.username = f"{form.cleaned_data['first_name']}.{form.cleaned_data['last_name']}".lower()
        user.save()

        if not change:
            address = Address.objects.create(
                street_address=form.cleaned_data['street_address'],
                city=form.cleaned_data['city'],
                country=form.cleaned_data['country'],
                zip_code=form.cleaned_data['zip_code']
            )
            user_profile = UserProfile.objects.create(
                user=user, address=address, type=form.cleaned_data['type']
            )

            if form.cleaned_data['type'] == 'employee':
                EmployeeProfile.objects.create(user_profile=user_profile)

            elif form.cleaned_data['type'] == 'customer':
                CustomerProfile.objects.create(user_profile=user_profile)

        else:
            user.profile.type = form.cleaned_data['type']

            if not user.profile.address:
                address = Address.objects.create(
                    street_address=form.cleaned_data['street_address'],
                    city=form.cleaned_data['city'],
                    country=form.cleaned_data['country'],
                    zip_code=form.cleaned_data['zip_code']
                )
                user.profile.address = address

            else:
                user.profile.address.street_address = form.cleaned_data['street_address']
                user.profile.address.city = form.cleaned_data['city']
                user.profile.address.country = form.cleaned_data['country']
                user.profile.address.zip_code = form.cleaned_data['zip_code']
                user.profile.address.save()

            user.profile.save()

        return user
