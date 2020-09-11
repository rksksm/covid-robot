import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

TRIG = 23
ECHO = 24

print("distance measure in progress")

gpio.setup(TRIG, gpio.OUT)
gpio.setup(ECHO, gpio.IN)

gpio.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(2)

gpio.output(TRIG, True)
time.sleep(0.00001)
gpio.output(TRIG, False)

while gpio.input(ECHO) == 1:
	pulse_start = time.time()

while gpio.input(ECHO) == 1:
	pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = round(pulse_duration * 17150, 2)

print(f"Distance: {distance} cm")

gpio.cleanup()

