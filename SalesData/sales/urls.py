from django.urls import path
from .views import salesChart

urlpatterns = [
    path('sales-chart/', salesChart, name='sales_chart'),
]
