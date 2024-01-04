import pika

EXCHANGE = "direct_queue"
ROUTING_KEY = "IMPORTANT"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

channel.exchange_declare(
    exchange=EXCHANGE,
    exchange_type="direct"
)

result = channel.queue_declare(
    queue="",
    exclusive=True
)
queue_name = result.method.queue

channel.queue_bind(
    exchange=EXCHANGE,
    queue=queue_name,
    routing_key=ROUTING_KEY
)

channel.basic_consume(
    queue=queue_name,
    auto_ack=True,
    on_message_callback=lambda ch, method, properties, body: print(f"Received - {body}")
)

channel.start_consuming()
