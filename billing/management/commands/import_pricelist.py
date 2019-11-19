"""
Import pricelist from a csv.
"""
import csv
import sys

from django.core.management.base import BaseCommand

from billing.models import BillingItem

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            help="Specify pricelist file",
        )

    def handle(self, *a, **k):
        BillingItem.objects.all().delete()

        filename = sys.argv[-1]
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                try:
                    name        = row[0]
                    description = row[1]
                    price       = float(row[2])
                    commission  = float(row[3].split(' ')[0])

                    item = BillingItem(
                        name=name, description=description,
                        price=price, commission=commission
                    )
                    item.save()
                except:
                    pass #    The pricelist has demo data
