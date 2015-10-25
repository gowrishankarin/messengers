#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shankar
# @Date:   2015-10-25 19:37:53
# @Last Modified by:   Gowri Shankar
# @Last Modified time: 2015-10-25 19:58:27

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange = 'topic_logs', type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
	routing_key=routing_key,
	body=message)

print " [x' Sent %r:%r" % (routing_key, message)
connection.close()