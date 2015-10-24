#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shankar
# @Date:   2015-10-24 19:16:33
# @Last Modified by:   shankar
# @Last Modified time: 2015-10-24 19:58:15

import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:])
channel.basic_publish(exchange='', 
	routing_key='task_queue', 
	body=message,
	properties = pika.BasicProperties(
		delivery_mode = 2, # make message persistent
	))
print " [x] Sent %r" % (message,)