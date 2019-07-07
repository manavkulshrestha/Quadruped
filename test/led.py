from gpiozero import LED
import sys

argc = len(sys.argv)
if argc < 2:
    exit(argc)

pin = -1

try:
    pin = int(sys.argv[1])
except ValueError:
    exit(pin)

led = LED(pin)

led.on()
while True:
    continue
