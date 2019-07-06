
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT,initial=GPIO.LOW)
while True:
    GPIO.output(40,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(40,GPIO.LOW)
    sleep(0.5)
    
