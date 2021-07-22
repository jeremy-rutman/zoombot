# this is the easy part and hence left to last
# given input command, turn on the corresponding GPIO pin

import request
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
FWD_PIN = 27
REV_PIN = 28
LEFT_PIN = 39
RIGHT_PIN = 40
LIGHTS_PIN = 41
all_pins = [FWD_PIN,REV_PIN,LEFT_PIN,RIGHT_PIN]
for channel in all_pins:
    GPIO.setup(channel, GPIO.IN)
    GPIO.output(channel, GPIO.LOW)


def do_command(command):
    print(f'doing command {command}')
    if command == 'REV':
        GPIO.output(REV_PIN,GPIO.HIGH)
        for i in range(3):
            sleep(0.2)
            GPIO.output(LIGHTS_PIN,GPIO.HIGH)
            sleep(0.2)
            GPIO.output(LIGHTS_PIN,GPIO.LOW)
        GPIO.output(REV_PIN,GPIO.LOW)
    if command == 'FWD':
        #  YOUR CODE GOES HERE!!!


last_executed_command=(0,'F')
while(1):
    resp = request.get()
 #   print(resp)
    commands_list = [(t,c) for t,c in resp.items()] # conceivably this isnt ordered
    latest_command = commands_list[-1]
    if latest_command[0] > last_executed_command[0]+0.01:
        lag = time.time() - latest_command[0]
        print(f'lag {lag}')
        do_command(latest_command)
        last_executed_command=latest_command

