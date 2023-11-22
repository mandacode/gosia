from django.db import models

from works.models import Customer, Employee


class ScratchpadRecord(models.Model):
    """Copy of work instance for scratchpad purposes."""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employees = models.ManyToManyField(Employee)
    date = models.DateField()
    hours = models.DecimalField(max_digits=4, decimal_places=2)

    def __repr__(self):
        return f"<ScratchpadRecord: {self.pk} | {self.date}>"


class Scratchpad(models.Model):
    """Scratchpad is a collection of scratchpad records."""
    start_date = models.DateField()
    end_date = models.DateField()
    records = models.ManyToManyField(ScratchpadRecord)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Scratchpad: {self.pk}>"