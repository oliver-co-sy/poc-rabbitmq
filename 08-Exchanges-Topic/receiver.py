import pika

EXCHANGE = "topic_exchange"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

channel.exchange_declare(
    exchange=EXCHANGE,
    exchange_type="topic"
)

result = channel.queue_declare(
    queue="",
    exclusive=True
)
queue_name = result.method.queue

# Routing key wildcards:
#   * - matches one word
#   # - matches zero or more words
channel.queue_bind(
    exchange=EXCHANGE,
    queue=queue_name,
    routing_key="school.#"
)

channel.basic_consume(
    queue=queue_name,
    auto_ack=True,
    on_message_callback=lambda ch, method, properties, body: print(f"Received - {body}")
)

channel.start_consuming()
