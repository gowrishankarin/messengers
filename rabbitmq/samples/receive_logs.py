#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gowri Shankar
# @Date:   2015-10-24 20:34:01
# @Last Modified by:   Gowri Shankar
# @Last Modified time: 2015-10-24 20:41:10


import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', type='fanout')


result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print " [*] Waiting for messages. To exit press CTRL+C"

def callback(ch, method, properties, body):
	print " [x] Received %r" % (body,)
	time.sleep(body.count('.'))
	print " [x] Done"
	channel.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue=queue_name)
channel.start_consuming()