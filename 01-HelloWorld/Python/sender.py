import pika

QUEUE = "hello"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

# Create a queue first otherwise the message will be dropped by RabbitMQ
# This method is idempotent
channel.queue_declare(queue=QUEUE)

# In RabbitMQ, messages are not sent directly to the queue, instead, messages are sent to an exchange.
# Using a default exchange - "" allows you to specify the queue as the routing_key parameter
channel.basic_publish(
    exchange="",
    routing_key=QUEUE,
    body="Hello World!"
)

connection.close()
