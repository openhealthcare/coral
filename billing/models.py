"""
Models for the Coral billing app
"""
from django.db import models
from opal.models import Patient


class BillingItem(models.Model):
    """
    An individual item that may be billed for
    """
    name        = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=200)
    price       = models.FloatField(blank=True, null=True)
    commission  = models.FloatField(blank=True, null=True)



class Bill(models.Model):
    """
    A list of items a patient is to be billed for
    """
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    items   = models.ManyToManyField(BillingItem)
    paid    = models.BooleanField(default=False)

    def value(self):
        return sum([item.price for item in self.items.all()])
