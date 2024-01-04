import pika

QUEUE = "ack_queue"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

channel.queue_declare(queue=QUEUE)

for msg_num in range(1, 10):
    channel.basic_publish(
        exchange="",
        routing_key=QUEUE,
        body=f"This is message number - {msg_num}"
    )

connection.close()
