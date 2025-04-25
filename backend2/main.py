#!/home/abc/flask_sandbox/message_queue/backend2/.venv/bin/python
import pika, sys

print("IM A PRODUCER")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare a new queue
channel.queue_declare(queue='task_queue', durable=True)


# Send a message to the queue
def send_message():
    message = ' '.join(sys.argv[1:]) or 'hi'
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        )
    )

# Send a message to the queue
send_message()

connection.close()
