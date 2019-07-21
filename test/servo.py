from gpiozero import Servo
import sys
from time import sleep

argc = len(sys.argv)
if argc < 2:
    exit(argc)

pin = -1

try:
    pin = int(sys.argv[1])
except ValueError:
    exit(pin)

servo = Servo(pin)

while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
    servo.mid()
