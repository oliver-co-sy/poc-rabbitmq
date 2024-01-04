import pika

EXCHANGE = "direct_queue"
ROUTING_KEY = "IMPORTANT"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

channel.exchange_declare(
    exchange=EXCHANGE,
    exchange_type="direct"
)

channel.basic_publish(
    exchange=EXCHANGE,
    routing_key=ROUTING_KEY,
    body="This is an important message"
)

connection.close()
