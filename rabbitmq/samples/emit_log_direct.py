#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gowri Shankar
# @Date:   2015-10-24 23:22:53
# @Last Modified by:   Gowri Shankar
# @Last Modified time: 2015-10-24 23:26:24

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World'


channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)

print " [x] Sent %r:%r" % (severity, message)
connection.close()