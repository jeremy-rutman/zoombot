# this is the easy part and hence left to last
# given input command, turn on the corresponding GPIO pin

# import RPi.GPIO as rpi
# import RPi
#rpi.VERSION

import request


print('hello')

while(1):
    resp = request.get()
    print(resp.content)