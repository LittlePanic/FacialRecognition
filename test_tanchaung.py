#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = '方昕成'


def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')


RPi.GPIO.setmode(GPIO.BOARD)
RPi.GPIO.setup(11, RPi.GPIO.IN)
GPIO.add_event_detect(11, GPIO.RISING, callback=my_callback)

