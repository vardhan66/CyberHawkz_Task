# Create a script in sales/management/commands/add_dummy_data.py

from django.core.management.base import BaseCommand
from sales.models import SalesData
from datetime import date
import random

class Command(BaseCommand):
    help = 'Add dummy sales data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        SalesData.objects.all().delete()  
        for month in range(1, 13):
            # Random number of entries per month
            for _ in range(random.randint(5, 15)): 
                SalesData.objects.create(
                    saleDate=date(2023, month, random.randint(1, 28)),
                    amount=random.uniform(100.00, 5000.00)
                )
        self.stdout.write(self.style.SUCCESS('Successfully added dummy data'))
