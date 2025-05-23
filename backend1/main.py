import pika, sys, os, time

print("IM A CONSUMER")

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
        print(f"Received message: {body.decode()}")
        time.sleep(body.count(b'.'))
        print("Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue='task_queue',
        on_message_callback=callback
    )

    # Start the message queue system
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
