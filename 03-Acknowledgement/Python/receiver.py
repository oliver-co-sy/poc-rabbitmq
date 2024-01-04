import pika

QUEUE = "ack_queue"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

channel.queue_declare(queue=QUEUE)

received_count = 0


def on_message(ch, method, properties, body):
    global received_count
    received_count += 1
    if received_count % 2:
        print(f"Acknowledging {body}")
        print(method.delivery_tag)
        channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(
    queue=QUEUE,
    on_message_callback=on_message
)

channel.start_consuming()
