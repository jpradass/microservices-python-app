import pika, json

params = pika.URLParameters('amqp://guest:guest@amqp:5672/host?heartbeat=600')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)