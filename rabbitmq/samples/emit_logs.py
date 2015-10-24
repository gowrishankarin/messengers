#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gowri Shankar
# @Date:   2015-10-24 20:34:01
# @Last Modified by:   Gowri Shankar
# @Last Modified time: 2015-10-24 20:36:55

import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', type='fanout')


message = ' '.join(sys.argv[1:])
channel.basic_publish(exchange='logs', 
	routing_key='', 
	body=message,
	properties = pika.BasicProperties(
		delivery_mode = 2, # make message persistent
	))
print " [x] Sent %r" % (message,)

connection.close()