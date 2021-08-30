#!/usr/bin/env python
import pika, sys, os
import argparse
import requests
import json
from six.moves.urllib.parse import urlencode


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--jenkins_url", required=True)
    arg_parser.add_argument("--jenkins_username", required=True)
    arg_parser.add_argument("--jenkins_password", required=True)
    arg_parser.add_argument("--target_job_name", required=True)
    arg_parser.add_argument("--queue_name", required=True)
    arg_parser.add_argument("--message_server_host", required=True)
    arg_parser.add_argument("--message_server_user", default="guest")
    arg_parser.add_argument("--message_server_pass", default="guest")
    args = arg_parser.parse_args()

    jenkins_url: str = args.jenkins_url
    jenkins_username: str = args.jenkins_username
    jenkins_password: str = args.jenkins_password
    target_job_name: str = args.target_job_name
    queue_name: str = args.queue_name

    host_addr = args.message_server_host

    credentials = pika.PlainCredentials(args.message_server_user, args.message_server_pass)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host_addr, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        message_data = json.loads(body.decode())
        print(" [x] Received message : %r" % message_data, flush=True)
        try:
            # Check Build Condition from message
            agent_label_value = message_data['label']
            job_url = f"{jenkins_url}job/{target_job_name}"
            build_params = {"run_on": agent_label_value}
            # Prepare Jenkins build url with parameters
            job_build_url = f"{job_url}/buildWithParameters?" + urlencode(build_params)
            print(f"Calling {job_build_url} ....", flush=True)
            r = requests.post(job_build_url, auth=(jenkins_username, jenkins_password))
            print(f"Status code is {r.status_code}", flush=True)
        except json.decoder.JSONDecodeError as err:
            print("INFO: This message does not contain JSON content", flush=True)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
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
