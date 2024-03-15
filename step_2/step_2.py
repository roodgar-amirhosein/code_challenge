from kafka import KafkaProducer, KafkaConsumer
import csv
import json


def fill_kafka_topic():
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    with open('price_data.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            data = {'Time': row['Time'], 'Stock': row['Stock'], 'Price': row['Price']}
            producer.send('main_topic', value=data)

    producer.close()


fill_kafka_topic()
print("Data sent to Kafka")

bootstrap_servers = 'localhost:9092'
topic = 'main_topic'

consumer = KafkaConsumer(topic,
                         bootstrap_servers=bootstrap_servers,
                         auto_offset_reset='earliest',
                         enable_auto_commit=False)

for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")

consumer.close()


