import pika

QUEUE = "fair_dispatch"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

channel.queue_declare(queue=QUEUE)

for _ in range(5):
    channel.basic_publish(
        exchange="",
        routing_key=QUEUE,
        body=f"This is a new message"
    )

connection.close()
