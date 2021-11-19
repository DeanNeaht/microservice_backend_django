import pika


params = pika.URLParameters('amqps://wvmozvxz:CJH8LLByzoJ41YKKgmS5fbXaslTRrRLW@woodpecker.rmq.cloudamqp.com/wvmozvxz')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='django_backend', body='hello')

