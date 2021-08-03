#!/usr/bin/env python
import pika
from datetime import datetime

host_addr = "127.0.0.1"
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host_addr))
channel = connection.channel()
channel.queue_declare(queue='hello')
message = f"Hello world at {datetime.now()}"
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f" [x] Sent {message}")
connection.close()