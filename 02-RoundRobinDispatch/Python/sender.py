import pika

QUEUE = "work_queue"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

channel.queue_declare(queue=QUEUE)

channel.basic_publish(
    exchange="",
    routing_key=QUEUE,
    body="This is the message"
)

connection.close()
