#!/usr/bin/env python
import pika
from datetime import datetime
import json
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--message_server_host", default="127.0.0.1")
arg_parser.add_argument("--label", default="gpu")
args = arg_parser.parse_args()
host_addr = args.message_server_host

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host_addr))
channel = connection.channel()
channel.queue_declare(queue='hello')
message: str = {"label": args.label}
channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(message))
print(f" [x] Sent {message}")
connection.close()
