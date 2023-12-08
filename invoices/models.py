from django.db import models


# class Record(models.Model):
#
#     date = models.DateField()
#     hours = models.DecimalField(max_digits=4, decimal_places=2)
#
#
# class CustomerInvoice(models.Model):
#
#     number = models.CharField(max_length=255)
#     date = models.DateField()
#     header = models.TextField(default="Rechnungsnummer:")
#     location = models.CharField(default="Berlin")
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)