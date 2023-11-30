from django.contrib import admin

from users.models import User, UserType
from .models import Work


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('the_customer', 'the_employees', 'hours', 'date', 'created_at')

    def the_employees(self, obj):
        return ', '.join([e.full_name for e in obj.employees.all()])

    def the_customer(self, obj):
        return obj.customer.full_name

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "employees":
            kwargs["queryset"] = User.objects.filter(profile__type=UserType.EMPLOYEE)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['customer'].queryset = User.objects.filter(profile__type=UserType.CUSTOMER)
        return form
