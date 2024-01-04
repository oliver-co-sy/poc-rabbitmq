import time

import pika

QUEUE = "fair_dispatch"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()
channel.queue_declare(queue=QUEUE)

channel.basic_qos(prefetch_count=1)


def on_message(ch, method, properties, body):
    print(f"Processing - {body}")
    time.sleep(3)
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(
    queue=QUEUE,
    on_message_callback=on_message
)

channel.start_consuming()
