# Code Challenge: Python-Django Backend

A sample microservice project with Django, Redis and Kafka to test your familiarities with these tools.

### Requirements

You need [Docker](https://docs.docker.com/get-docker/) installed on you machine to run **Redis** and **Apache Kafka** instances. [Python](https://www.python.org/downloads/) is also needed for various scripts in all the steps.

### Included in the Box

Sample price data for three fictional stocks needed in the next steps are stored in `price_data.csv`. In `./redis` folder there is a docker-compose file for running a dockerized Redis database instance. Similarly, the docker-compose file for starting a dockerized instance of message queuing system Kafka is found in `./kafka` folder. This docker-compose file initializes a topic named `main_topic` after startup.

## Step 1: Price Updater Service

Write a price updater service with Python that accomplishes these tasks:

- Reads the price data in `price_data.csv` for **Stock1**, **Stock2** and **Stock3** starting from 9:00:00 to 9:59:47
- Connects to the Redis database
- For each data row, updates the time and price history of the corresponding stock

> **Note:** Make sure Redis database is running and is accessible on `localhost` on default port `6037`

> **Hint:** The stock price history data in stored in Redis in `key`-`value` format. The key value for Stock1, Stock2 and Stock3 are `stock1`, `stock2` and `stock3` respectively. The value is in json format in which the `time` field is a list of timestamps `hhmmss`. The `price` field is the list of stock prices at respective timestamps.

> **Note:** Price history is a minute-wise time series, so price values for each minute is required.

Finally, dockerize your script to be used as a standalone service.

## Step 2: It's Message Queueing Time!

In this Step we want to integrate Apache Kafka in our project, so, instead of reading the data from the `price_data.csv` file, we will be listening to a Kafka topic and get the stock price data from there.

> **Note:** Make sure Kafka is running and is accessible on `localhost` on port `9092` and the topic `main_topic` is available.

First you need to fill the Kafka `main_topic` with the price data given in `price_data.csv`. Create a `KafkaProducer`, then read the data from `price_data.csv` and send it to the `main_topic`.

Now that the data is saved in Kafka, repeat the task in Step 1, but use a `KafkaConsumer` to get the price data.

## Step 3: Django and DRF

The goal in this step is to create a `BuyStock` API endpoint in Django and do a basic check on the request.

Start an empty Django project and make sure `rest_framework` is installed. Create an API endpoint named `BuyStock` which accepts a **Post** request from user. The body content is a valid json object in this form as an example:

```
{
	"user": "user2",
	"stockname": "stock1",
	"quantity" : 100
}
```

This request needs to be verified and a proper response needs to be sent back.
First connect to the Redis database and get the user data for this user. If the user credit is enough to buy this stock in this quantity return `Accept`, otherwise return `Deny`.

Finally, write **Unit Tests** and **Integration Tests** for your API to make sure it's working correctly.

## Step 4: Save and Retrieve

In this final step we want to use django ORM to save user orders and retrieve this data. First, create a model named `Orders` with fields

- user: either `user1` or `user2`
- stock: either `stock1` or `stock2` or `stock3`
- status: either `accepted` or `denied`
- creation_date: date and time of the order creation
- price: positive Integer
- quantity: positive Integer

Returning back to **Step 3**, add the functionality to the `BuyStock` endpoint to save the received order.

Now implement a Django REST API endpoint using Django REST Framework to fetch orders that meet the following criteria: The status is either `accepted` or the order is created today. Exclude orders where the status is `denied` and the quantity is smaller than 10. Ensure the API endpoint returns the ordered results by the `creation_date` field in descending order.

Write unit tests for the API endpoint to verify its functionality.
# code_challenge
# code_challenge
# code_challenge
# code_challenge
