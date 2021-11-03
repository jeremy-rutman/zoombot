# this is the easy part and hence left to last
# given input command, turn on the corresponding GPIO pin

import request
import time
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
camera=PiCamera()
time.sleep(2)
import subprocess

GPIO.setmode(GPIO.BOARD)
FWD_PIN = 22  # if you remember the correct pins , you can change these
REV_PIN = 21
LEFT_PIN = 13
RIGHT_PIN = 32
LIGHTS_PIN = 37
all_pins = [FWD_PIN,REV_PIN,LEFT_PIN,RIGHT_PIN,LIGHTS_PIN]

for channel in all_pins:
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)


def do_command(instruction):
    print(f'doing command {instruction}')
    time = instruction[0]
    command = instruction[1]
    if command == 'B':
        print('going backwards')
        GPIO.output(REV_PIN,GPIO.HIGH)
        for i in range(3):
            sleep(0.2)
            GPIO.output(LIGHTS_PIN,GPIO.HIGH)
            sleep(0.2)
            GPIO.output(LIGHTS_PIN,GPIO.LOW)
        GPIO.output(REV_PIN,GPIO.LOW)
    if command == 'F':
        #  YOUR CODE GOES HERE!!!
        GPIO.output(FWD_PIN, GPIO.HIGH)
        sleep(2)
        GPIO.output(FWD_PIN, GPIO.LOW)
    if command=='R':
        GPIO.output(RIGHT_PIN, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(RIGHT_PIN, GPIO.LOW)
    if command=='L':
        GPIO.output(LEFT_PIN, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(LEFT_PIN, GPIO.LOW)
    if command=='PiCamera':
        camera.capture("/home/pi/pictures/img.jpg")
        cmd=f'scp -o StrictHostKeyChecking=no -i /home/pi/zoombot/keyfile /home/pi/pictures/img.jpg root@178.128.26.70:/home/ubuntu/zoombot/image.jpg'
        retval=subprocess.run(cmd,shell=True)
        print(retval)

def safe_off():
    for pin in all_pins:
       GPIO.output(pin, GPIO.LOW)

last_executed_command=(0,'F')
while(1):
    resp = request.get()
    print(resp)
    commands_list = [(t,c) for t,c in resp.items()] # conceivably this isnt ordered
    latest_command = commands_list[-1]
    if latest_command[0] > last_executed_command[0]+0.01:
        lag = time.time() - latest_command[0]
        print(f'lag {lag}')
        do_command(latest_command)
        last_executed_command=latest_command

