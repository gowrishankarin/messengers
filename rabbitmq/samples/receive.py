#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shankar
# @Date:   2015-10-24 18:59:10
# @Last Modified by:   shankar
# @Last Modified time: 2015-10-24 19:07:34

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

print " [*] Waiting for messages. To exit press CTRL+C"


def callback(ch, method, properties, body):
	print " [x] Received %r" % (body,)

channel.basic_consume(callback, queue='hello', no_ack=True)
channel.start_consuming()