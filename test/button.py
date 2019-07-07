from gpiozero import Button
import sys

argc = len(sys.argv)
if argc < 2:
    exit(argc)

pin = -1

try:
    pin = int(sys.argv[1])
except ValueError:
    exit(pin)    

button = Button(pin)
count = 1

def button_action():
    global count
    print(count)
    count += 1

button.when_pressed = button_action

while True:
    continue
