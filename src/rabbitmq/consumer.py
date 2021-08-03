#!/usr/bin/env python
import pika, sys, os
import argparse

jenkins_url = os.environ['JENKINS_URL']
jenkins_username = os.environ['JENKINS_USERNAME']
jenkins_psasword = os.environ['JENKINS_PASSWORD']
target_job_name = os.environ['TARGET_JOB_NAME']

def main(host_addr):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host_addr))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        job_url = f"{jenkins_url}/job/{target_job_name}"
        job_bulid_url = f"{job_url}/buildWithParameters"
        print(job_bulid_url)
        print(" [x] Received %r" % body.decode())

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--message_server_host", default="127.0.0.1")
    args = arg_parser.parse_args()
    try:
        main(args.message_server_host)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
