import pika

QUEUE = "durable_queue"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()
channel.queue_declare(
    queue=QUEUE,
    durable=True
)

channel.basic_consume(
    queue=QUEUE,
    auto_ack=True,
    on_message_callback=lambda ch, method, properties, body: print(f"Received - {body}")
)

channel.start_consuming()
