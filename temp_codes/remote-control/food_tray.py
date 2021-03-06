from time import sleep
import time
import RPi.GPIO as gpio
import json

config_file = open("config.json", 'r')
configuration = json.loads(config_file.read())["food_tray"]
print(configuration)


def setup():
	# setting up the RaspberryPi modes
	gpio.setwarnings(False)  # Ignore warning for now
	gpio.setmode(gpio.BCM)  # Use physical pin numbering

	# setting up IR_sensor
	gpio.setup(configuration['IR_sensor'], gpio.IN)

	# setting up the motor 1
	gpio.setup(configuration['motor_1_direction_pin'], gpio.OUT)
	gpio.setup(configuration['motor_1_step_pin'], gpio.OUT)

	# setting up the motor 2
	gpio.setup(configuration['motor_2_direction_pin'], gpio.OUT)
	gpio.setup(configuration['motor_2_step_pin'], gpio.OUT)

	# setting up cut switches
	gpio.setup(configuration['top_switch'], gpio.IN, pull_up_down=gpio.PUD_DOWN)  # top switch
	gpio.setup(configuration['bottom_switch'], gpio.IN, pull_up_down=gpio.PUD_DOWN)  # bottom Switch
	gpio.setup(configuration['refill'], gpio.IN, pull_up_down=gpio.PUD_DOWN)  # top switch
	gpio.setup(configuration['use'], gpio.IN, pull_up_down=gpio.PUD_DOWN)  # bottom Switch


def motor_rotate(rotate = False):
	if rotate:
		gpio.output(configuration['motor_1_step_pin'], gpio.HIGH)
		gpio.output(configuration['motor_2_step_pin'], gpio.HIGH)
		sleep(.0002)
		gpio.output(configuration['motor_1_step_pin'], gpio.LOW)
		gpio.output(configuration['motor_2_step_pin'], gpio.LOW)
		sleep(.0002)


operating_mode = ''
setup()
while True:
	if gpio.input(configuration['use']):
		operating_mode = 'use'
	if gpio.input(configuration['refill']):
		operating_mode = 'refill'
		
	print(operating_mode)
	if operating_mode == 'refill':
		gpio.output(configuration['motor_1_direction_pin'], configuration["direction_down"])
		gpio.output(configuration['motor_2_direction_pin'], configuration["direction_down"])
		if gpio.input(configuration['bottom_switch']) == gpio.HIGH:
			motor_rotate(rotate=False)
			operating_mode = ''
		if not gpio.input(configuration['IR_sensor']):
			motor_rotate(rotate=True)
	if operating_mode == 'use':
		gpio.output(configuration['motor_1_direction_pin'], configuration["direction_up"])
		gpio.output(configuration['motor_2_direction_pin'], configuration["direction_up"])
		if gpio.input(configuration['top_switch']) == gpio.HIGH:
			motor_rotate(rotate=False)
			operating_mode = ''
		if gpio.input(configuration['IR_sensor']):
			motor_rotate(rotate=True)
		if not gpio.input(configuration['IR_sensor']):
			motor_rotate(rotate=False)
