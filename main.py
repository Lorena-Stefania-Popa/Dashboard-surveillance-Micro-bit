# Add your Micro:bit Python code here. E.g.
from microbit import *
import utime

while True:
    msg = str(temperature()) + "\n"
    uart.write(msg)
    msg2 = str(display.read_light_level()) + "\n"
    uart.write(msg2)
    utime.sleep(30)