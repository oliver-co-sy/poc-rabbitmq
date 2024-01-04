import pika

QUEUE = "durable_queue"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

channel.queue_declare(
    queue=QUEUE,
    durable=True
)

channel.basic_publish(
    exchange="",
    routing_key=QUEUE,
    body="This is a durable message",
    properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent)
)

connection.close()
