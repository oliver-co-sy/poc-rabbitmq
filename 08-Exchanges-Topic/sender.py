import pika

EXCHANGE = "topic_exchange"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", port=8000))
channel = connection.channel()

channel.exchange_declare(
    exchange=EXCHANGE,
    exchange_type="topic"
)

channel.basic_publish(
    exchange=EXCHANGE,
    routing_key="school.staff.teacher",
    body="Sending to all teachers"
)

channel.basic_publish(
    exchange=EXCHANGE,
    routing_key="school.student.elementary",
    body="Sending to all elementary students"
)

connection.close()
