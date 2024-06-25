from django.shortcuts import render
from django.db.models import Sum
from django.core.cache import cache
from sales.models import SalesData
import json

def salesChart(request):
    # Key for caching the sales data
    cacheKey = 'monthlySalesData'  
    # To get the cached data
    salesData = cache.get(cacheKey)  

    if not salesData:
        # If cache is empty, query the database
        salesData = SalesData.objects.values('saleDate__year', 'saleDate__month')\
            .annotate(totalAmount=Sum('amount'))\
            .order_by('saleDate__year', 'saleDate__month')
        
        # Convert Decimal objects to strings for JSON serialization
        salesData = [
            {
                'saleDate__year': data['saleDate__year'],
                'saleDate__month': data['saleDate__month'],
                # Convert Decimal to string
                'totalAmount': str(data['totalAmount'])  
            }
            for data in salesData
        ]
        
        # Cache the data for 1 hour (3600 seconds)
        cache.set(cacheKey, salesData, 3600)  
    context = {
        # Serialize the sales data to JSON format
        'salesData': json.dumps(salesData)  
    }
    # Render the template with the sales data context
    return render(request, 'sale_chart.html', context)  
