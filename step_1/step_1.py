import csv
import redis
import json

r = redis.Redis(host='redis', port=6379, db=0)

last_prices = {}

with open('price_data.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        time = row['Time']
        stock = row['Stock']
        price = row['Price']

        hour = int(time[:2])
        minute = int(time[2:4])
        time_str = f"{hour:02d}:{minute:02d}"

        if stock not in last_prices:
            last_prices[stock] = {}

        last_prices[stock][time_str] = price

time_range = [f"{hour:02d}:{minute:02d}" for hour in range(9, 10) for minute in range(0, 58)]

stock_data = {}
id_mapping = {'stock1': 1, 'stock2': 2, 'stock3': 3}

for stock, prices in last_prices.items():
    stock_id = id_mapping[stock]
    if stock_id not in stock_data:
        stock_data[stock_id] = {'id': stock_id, 'price': [], 'time': [], 'performance': 0}

    for time in time_range:
        stock_data[stock_id]['time'].append(time)

        if time in prices:
            stock_data[stock_id]['price'].append(int(prices[time]))
        elif len(stock_data[stock_id]['price']) > 0:
            stock_data[stock_id]['price'].append(stock_data[stock_id]['price'][-1])
        else:
            stock_data[stock_id]['price'].append(0)


for stock_id, data in stock_data.items():
    r.set(f'stock{stock_id}', json.dumps(data))


