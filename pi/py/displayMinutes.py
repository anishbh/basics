import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime

GpioPinsA = [3,5,7,8,10,11,12]
GpioPinsB = [13,15,16,18,19,21,22]

letters = {"A": 3, "B":5, "C":7, "D":8, "E":10, "F":11, "G":12, \
           'a':13, 'b':15, 'c':16,'d':18,'e':19, 'f':21,'g':22}

keysA = {0:['A','B','C','D','E','F'],1:['B','C'],2:['A','B','G','E','D'], \
         3: ['A','B','C','D','G'],4:['F','G','B','C'],5:['A','F','G','C','D'], \
         6:['A','C','D','E','F','G'],7:['A','B','C'],8:['A','B','C','D','E','F','G'],\
         9:['A','B','C','F','G']}

keysB = {0:['A','B','C','D','E','F'],1:['B','C'],2:['A','B','G','E','D'],\
         3: ['A','B','C','D','G'],4:['F','G','B','C'],5:['A','F','G','C','D'],\
         6:['A','C','D','E','F','G'],7:['A','B','C'],8:['A','B','C','D','E','F','G'],\
         9:['A','B','C','F','G']}

for key in keysB:
    counter = 0
    for i in keysB.get(key):
        keysB.get(key)[counter] = i.lower()
        counter += 1

def setup():
    GPIO.setwarnings( False )
    GPIO.setmode( GPIO.BOARD )
    for pin in GpioPinsA:
        GPIO.setup(pin,GPIO.OUT,initial=GPIO.HIGH)
    for pin in GpioPinsB:
        GPIO.setup(pin,GPIO.OUT,initial=GPIO.HIGH)



def displayNumber(display,num):
    clear()
    if display == "DISPLAY0":
        for i in (letters.get(key) for key in keysA.get(num)):
            GPIO.output(i,GPIO.LOW)
    if display == "DISPLAY1":
        for i in (letters.get(key) for key in keysB.get(num)):
            GPIO.output(i,GPIO.LOW)

def clear():
    for pin in GpioPinsA:
        GPIO.output(pin,GPIO.HIGH)
    for pin in GpioPinsB:
        GPIO.output(pin,GPIO.HIGH)

def main():
    setup()
    while (True):
        minutes = datetime.now().minute
        minuteList = [int(a) for a in str(minutes)]
        if len(minuteList) == 2:
            displayNumber('DISPLAY0', minuteList[0])
            displayNumber('DISPLAY1', minuteList[1])
        else:
            displayNumber('DISPLAY0', 0)
            displayNumber('DISPLAY1', minuteList[0])

main()
