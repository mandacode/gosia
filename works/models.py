from django.db import models

from users.models import Address


class CustomerType(models.TextChoices):
    PRIVATE = 'private'
    COMPANY = 'company'


class Person(models.Model):

    name = models.CharField(max_length=255)
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.name}"


class Customer(Person):

    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, default=15.00)


class Employee(Person):

    nip = models.CharField(max_length=10)


class Work(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employees = models.ManyToManyField(Employee, related_name='works')
    date = models.DateField()
    hours = models.DecimalField(max_digits=4, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Work: {self.customer.name} {self.date} {self.hours}h>"
