# this is the easy part and hence left to last
# given input command, turn on the corresponding GPIO pin

# import RPi.GPIO as rpi
# import RPi
#rpi.VERSION

import request
import time

def do_command(command):
    print(f'doing command {command}')

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

