import redis
from code_challenge_django.settings import REDIS_HOST, REDIS_PORT
import json
from .models import Orders


def connect_to_redis():
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    return redis_client


def get_user_credit(redis_client, user):
    user_data = redis_client.get(user)
    if user_data is not None:
        user_data = json.loads(user_data)
        user_credit = user_data['credit']
        return user_credit
    else:
        return None


def get_stock_latest_price(redis_client, stockname):
    stock_data = redis_client.get(stockname)
    if stock_data is not None:
        stock_data = json.loads(stock_data)
        stock_latest_price = stock_data["price"][-1]

        return stock_latest_price
    else:
        return None


def can_user_pay(user_credit, stock_latest_price, quantity):
    if user_credit >= (stock_latest_price * quantity):
        return True
    return False


def create_order(user, stockname, status, price, quantity):
    if status:
        result = "accepted"
    else:
        result = "denied"

    order = Orders(user=user, stock=stockname, status=result, price=price, quantity=quantity)
    order.save()
