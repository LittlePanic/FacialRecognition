import RPi.GPIO as GPIO
import time
import os



def my_callback(channel):
    print('sssssssssss')
    os.system('python face_recognition_system.py')

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)

GPIO.add_event_detect(12, GPIO.RISING, callback=my_callback,bouncetime=40000)
while(True):
    pass
GPIO.cleanup()