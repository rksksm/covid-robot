from time import sleep
import time
import RPi.GPIO as gpio
import json

config_file = open("../../config.json", 'r')
configuration = json.loads(config_file.read())["medicine_tray"]
print(configuration)


def setup():
	# setting up the RaspberryPi modes
	gpio.setwarnings(False)  # Ignore warning for now
	gpio.setmode(gpio.BCM)  # Use physical pin numbering

	# setting up the motor 1
	gpio.setup(configuration['motor_1_direction_pin'], gpio.OUT)
	gpio.setup(configuration['motor_1_step_pin'], gpio.OUT)
	gpio.output(configuration['motor_1_direction_pin'], configuration["direction_left"])


def motor_rotate(pause=False):
	if not pause:
		gpio.output(configuration['motor_1_step_pin'], gpio.HIGH)
		sleep(.001)
		gpio.output(configuration['motor_1_step_pin'], gpio.LOW)
		sleep(.001)


def run_program(steps):
	setup()
	print("setup completed")
	counter = 0
	while counter < steps:
		motor_rotate(pause=False)
		counter += 1
