#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: shankar
# @Date:   2015-10-24 18:59:10
# @Last Modified by:   shankar
# @Last Modified time: 2015-10-24 19:01:54

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

print "Message Sent!!"

connection.close()