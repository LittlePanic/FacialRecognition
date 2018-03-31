import RPi.GPIO as GPIO
import time

#测试11针脚电流变化

RPi.GPIO.setmode(GPIO.BOARD)
RPi.GPIO.setup(11, RPi.GPIO.OUT)

while (True):
    GPIO.output(11, 1)
    time.sleep(1)
    GPIO.output(11, 0)
    time.sleep(1)

GPIO.cleanup()


#GPIO.setwarnings(False)  #RPi.GRIO检测到一个引脚已经被设置成了非默认值,禁用警告


