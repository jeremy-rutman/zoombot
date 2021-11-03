from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)


for i in range (10):
    GPIO.output(32, GPIO.HIGH)
    sleep(2)
    GPIO.output(32, GPIO.LOW)
    sleep(2)
    GPIO.output(11, GPIO.HIGH)
    sleep(2)
    GPIO.output(11, GPIO.LOW)
    sleep(2)


    GPIO.output(21, GPIO.HIGH)
    sleep(2)
    GPIO.output(21, GPIO.LOW)
    sleep(2)
    GPIO.output(22, GPIO.HIGH)
    sleep(2)
    GPIO.output(22, GPIO.LOW)
    sleep(2)

GPIO.output(21, GPIO.HIGH)
GPIO.output(22, GPIO.LOW)
GPIO.output(32, GPIO.HIGH)
GPIO.output(11, GPIO.LOW)
