import pika

QUEUE = "hello"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

# Create a queue first otherwise the message will be dropped by RabbitMQ
# This method is idempotent
channel.queue_declare(queue=QUEUE)

channel.basic_consume(
    queue=QUEUE,
    on_message_callback=lambda ch, method, properties, body: print(f"Received - {body}"),
    auto_ack=True
)

# This is a blocking call
channel.start_consuming()
