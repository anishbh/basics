import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime

GpioPinsA = [3,5,7,8,10,11,12]
GpioPinsB = [13,15,16,18,19,21,22]
GpioDots  = [23,24]

segmentToPin = { "A": 3, "B": 5, "C": 7, "D": 8, "E":10, "F":11, "G":12,
                 'a':13, 'b':15, 'c':16, 'd':18, 'e':19, 'f':21, 'g':22 }

numberToSegment = { 0:['A','B','C','D','E','F'],
                       1:['B','C'],
                       2:['A','B','G','E','D'],
                       3:['A','B','C','D','G'],
                       4:['F','G','B','C'],
                       5:['A','F','G','C','D'], 
                       6:['A','C','D','E','F','G'],
                       7:['A','B','C'],
                       8:['A','B','C','D','E','F','G'],
                       9:['A','B','C','F','G'] }
#Set up all pins
def setup():
    GPIO.setwarnings( False )
    GPIO.setmode( GPIO.BOARD )
    for pin in GpioPinsA:
        GPIO.setup(pin,GPIO.OUT,initial=GPIO.LOW)
    for pin in GpioPinsB:
        GPIO.setup(pin,GPIO.OUT,initial=GPIO.LOW)
    for pin in GpioDots:
        GPIO.setup(pin,GPIO.OUT,initial=GPIO.LOW)

#Display number on specific display        
def displayNumber(display,num):
    clear(display)
    if display == "DISPLAY0":
        for pin in (segmentToPin[segment] for segment in numberToSegment[num]):
            GPIO.output(pin,GPIO.LOW)
    if display == "DISPLAY1":
        for pin in (segmentToPin[segment.lower()] for segment in numberToSegment[num]):
            GPIO.output(pin,GPIO.LOW)

#Clear specific display
def clear(display):
    if display == "DISPLAY0":
        for pin in GpioPinsA:
            GPIO.output(pin,GPIO.HIGH)
    if display == "DISPLAY1":        
        for pin in GpioPinsB:
            GPIO.output(pin,GPIO.HIGH)
 
def toggleDots(hour):
    if hour:
        for pin in GpioDots:
            GPIO.output(pin,GPIO.LOW)
    else:
        for pin in GpioDots:
            GPIO.output(pin,GPIO.HIGH)

def showMinutes():
    minutes = datetime.now().minute
    minuteList = [int(a) for a in str(minutes)]
    if len(minuteList) == 2:
        displayNumber('DISPLAY0', minuteList[0])
        displayNumber('DISPLAY1', minuteList[1])
    else:
        displayNumber('DISPLAY0', 0)
        displayNumber('DISPLAY1', minuteList[0])
    toggleDots(False)

def showHour():
    hours = datetime.now().hour
    hourList = [int(a) for a in str(hours)]
    if len(hourList) == 2:
        displayNumber('DISPLAY0', hourList[0])
        displayNumber('DISPLAY1', hourList[1])
    else:
        displayNumber('DISPLAY0', 0)
        displayNumber('DISPLAY1', hourList[0])
    toggleDots(True)

def main():
    setup()
    while True:
        showHour()
        sleep(2)
        showMinutes()
        sleep(2)

main()
