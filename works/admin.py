from django.contrib import admin

from .models import Work, Customer, Employee


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'hourly_rate', 'address')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'nip', 'address')


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'hours')
