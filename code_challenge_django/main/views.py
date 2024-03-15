from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BuyStockSerializer, OrdersSerializer
from .utils import (connect_to_redis,
                    get_user_credit,
                    get_stock_latest_price,
                    can_user_pay,
                    create_order)
from .models import Orders
import datetime
from django.db.models import Q


# Create your views here.
class BuyStockView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BuyStockSerializer(data=request.data)
        result = 'Deny'
        if serializer.is_valid():
            user = serializer.validated_data['user']
            stockname = serializer.validated_data['stockname']
            quantity = serializer.validated_data['quantity']

            redis_client = connect_to_redis()
            user_credit = get_user_credit(redis_client, user)
            stock_latest_price = get_stock_latest_price(redis_client, stockname)

            if user_credit is None or stock_latest_price is None:
                return Response(serializer.errors, status=400)

            buy_stock_result = can_user_pay(user_credit, stock_latest_price, quantity)

            create_order(
                user=user,
                stockname=stockname,
                status=buy_stock_result,
                price=stock_latest_price,
                quantity=quantity
            )

            if buy_stock_result:
                result = 'Accept'

            return Response({"result": result})
        else:
            return Response(serializer.errors, status=400)


class Fetch_orders(APIView):
    def get(self, request):
        today = datetime.datetime.now().date()

        orders = Orders.objects.filter(
            Q(status='Accepted') | Q(creation_date__date=today),
            ~Q(status='Denied'),
            ~Q(quantity__lt=10)
        ).order_by('-creation_date')

        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)
