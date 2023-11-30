from django.db import models

from users.models import User


class ScratchpadRecord(models.Model):

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_scratchpad_records')
    employees = models.ManyToManyField(User, related_name='employee_scratchpad_records')
    date = models.DateField()
    hours = models.DecimalField(max_digits=4, decimal_places=2)

    def __repr__(self):
        return f"<ScratchpadRecord: {self.pk} | {self.date}>"


class Scratchpad(models.Model):

    start_date = models.DateField()
    end_date = models.DateField()
    records = models.ManyToManyField(ScratchpadRecord)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Scratchpad: {self.pk}>"
