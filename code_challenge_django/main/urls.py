from django.urls import path
from .views import BuyStockView, Fetch_orders

urlpatterns = [
    path('BuyStock/', BuyStockView.as_view(), name='buy_stock'),
    path('fetch_orders', Fetch_orders.as_view(), name="fetch_orders")
]