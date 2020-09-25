from time import sleep
import RPi.GPIO as gpio
import json

config_file = open("../../config.json", 'r')
configuration = json.loads(config_file.read())["camera_tray"]
print(configuration)

motor_moving = False


def setup_forward():
	# setting up the RaspberryPi modes
	gpio.setwarnings(False)  # Ignore warning for now
	gpio.setmode(gpio.BCM)  # Use physical pin numbering

	# setting up the motor 1
	gpio.setup(configuration['motor_1_direction_pin'], gpio.OUT)
	gpio.setup(configuration['motor_1_step_pin'], gpio.OUT)
	gpio.output(configuration['motor_1_direction_pin'], configuration["direction_left"])

	# setting up cut switches
	gpio.setup(configuration['switch'], gpio.IN, pull_up_down=gpio.PUD_DOWN)  # switch


def setup_backward():
	# setting up the RaspberryPi modes
	gpio.setwarnings(False)  # Ignore warning for now
	gpio.setmode(gpio.BCM)  # Use physical pin numbering

	# setting up the motor 1
	gpio.setup(configuration['motor_1_direction_pin'], gpio.OUT)
	gpio.setup(configuration['motor_1_step_pin'], gpio.OUT)
	gpio.output(configuration['motor_1_direction_pin'], configuration["direction_left"])

	# setting up cut switches
	gpio.setup(configuration['switch'], gpio.IN, pull_up_down=gpio.PUD_DOWN)  # switch


def motor_rotate():
	gpio.output(configuration['motor_1_step_pin'], gpio.HIGH)
	sleep(.0002)
	gpio.output(configuration['motor_1_step_pin'], gpio.LOW)
	sleep(.0002)


def condition():
	if gpio.input(configuration['switch']) == gpio.HIGH:
		return False
	else:
		return True


def run_program(steps, direction):
	if direction == 'forward':
		setup_forward()
	if direction == 'backward':
		setup_backward()
	print("setup completed")
	counter = 0
	while counter < steps:
		motor_rotate()
		counter += 1
