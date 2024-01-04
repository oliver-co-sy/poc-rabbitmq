import time

import pika

EXCHANGE = "new_exchange"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

channel.exchange_declare(
    exchange=EXCHANGE,
    exchange_type="fanout"
)

for _ in range(10):
    channel.basic_publish(
        exchange=EXCHANGE,
        routing_key="",
        body="Sending this message to an exchange"
    )
    time.sleep(1)

connection.close()
