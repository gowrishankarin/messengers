#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shankar
# @Date:   2015-10-24 19:18:36
# @Last Modified by:   shankar
# @Last Modified time: 2015-10-24 20:02:51

import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print " [*] Waiting for messages. To exit press CTRL+C"

def callback(ch, method, properties, body):
	print " [x] Received %r" % (body,)
	time.sleep(body.count('.'))
	print " [x] Done"
	channel.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')
channel.start_consuming()