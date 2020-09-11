import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def distance():
	print("running")
	# set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER, True)

	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	StartTime = time.time()
	StopTime = time.time()

	# save StartTime
	while GPIO.input(GPIO_ECHO) == 1:
		StartTime = time.time()

	# save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()

	# time difference between start and arrival
	TimeElapsed = StopTime - StartTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2

	return distance


if __name__ == '__main__':
	try:
		while True:
			dist = distance()
			print("Measured Distance = %.1f cm" % dist)
			time.sleep(1)

	# Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		GPIO.cleanup()

# import RPi.GPIO as gpio
# import time
# gpio.setmode(gpio.BCM)
#
# TRIG = 23
# ECHO = 24
#
# print("distance measure in progress")
#
# gpio.setup(TRIG, gpio.OUT)
# gpio.setup(ECHO, gpio.IN)
#
# gpio.output(TRIG, False)
# print("Waiting for sensor to settle")
# time.sleep(2)
#
# gpio.output(TRIG, True)
# time.sleep(0.00001)
# gpio.output(TRIG, False)
#
# pulse_start = 0
# pulse_end = 0
#
# while gpio.input(ECHO) == 1:
# 	pulse_start = time.time()
# 	print("pulse started ", pulse_start)
#
# while gpio.input(ECHO) == 1:
# 	pulse_end = time.time()
# 	print("pulse end ", pulse_end)
#
# pulse_duration = pulse_end - pulse_start
#
# distance = round(pulse_duration * 17150, 2)
#
# print("Distance: "+str(distance)+" cm")
#
# gpio.cleanup()
