import pika

params = pika.URLParameters('amqp://guest:guest@admin_amqps_1:5672/host')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')