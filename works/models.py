from django.db import models
from django.contrib.auth.models import User


class Work(models.Model):

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    employees = models.ManyToManyField(User, related_name='works')
    date = models.DateField()
    hours = models.DecimalField(max_digits=4, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Work: {self.customer.full_name()} {self.date} {self.hours}h>"
