from django.db import models  


class SalesData(models.Model):
    # Date field for the sale date
    saleDate = models.DateField()
    
    # Decimal field for the sale amount 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.saleDate} - {self.amount}"
