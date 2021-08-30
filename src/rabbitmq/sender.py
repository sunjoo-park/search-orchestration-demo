#!/usr/bin/env python
import pika
from datetime import datetime
import json
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--message_server_host", default="127.0.0.1")
arg_parser.add_argument("--message_server_user", default="guest")
arg_parser.add_argument("--message_server_pass", default="guest")
arg_parser.add_argument("--queue_name", default="hello")
arg_parser.add_argument("--label", default="gpu")
args = arg_parser.parse_args()

host_addr: str = args.message_server_host
queue_name: str = args.queue_name

credentials = pika.PlainCredentials(args.message_server_user, args.message_server_pass)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host_addr, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue=queue_name)
message: str = {"label": args.label}
for i in range(1):
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
    print(f" [x] Sent {message}")
connection.close()
