from time import sleep
import RPi.GPIO as gpio
import json

config_file = open("../../config.json", 'r')
configuration = json.loads(config_file.read())["tray"]
print(configuration)

motor_moving = False


def setup():
	# setting up the RaspberryPi modes
	gpio.setwarnings(False)  # Ignore warning for now
	gpio.setmode(gpio.BCM)  # Use physical pin numbering

	# setting up the motor 1
	gpio.setup(configuration['motor_1_direction_pin'], gpio.OUT)
	gpio.setup(configuration['motor_1_step_pin'], gpio.OUT)
	gpio.output(configuration['motor_1_direction_pin'], configuration["direction_up"])

	# setting up the motor 2
	gpio.setup(configuration['motor_2_direction_pin'], gpio.OUT)
	gpio.setup(configuration['motor_2_step_pin'], gpio.OUT)
	gpio.output(configuration['motor_2_direction_pin'], configuration["direction_up"])

	# setting up cut switches
	gpio.setup(configuration['top_switch'], gpio.IN, pull_up_down=gpio.PUD_DOWN)  # top switch
	gpio.setup(configuration['bottom_switch'], gpio.IN, pull_up_down=gpio.PUD_DOWN)  # bottom Switch


def motor_rotate():
	gpio.output(configuration['motor_1_step_pin'], gpio.HIGH)
	gpio.output(configuration['motor_2_step_pin'], gpio.HIGH)
	sleep(.0002)
	gpio.output(configuration['motor_1_step_pin'], gpio.LOW)
	gpio.output(configuration['motor_2_step_pin'], gpio.LOW)
	sleep(.0002)


def start_condition():
	if gpio.input(configuration['top_switch']) == gpio.LOW and gpio.input(configuration['bottom_switch']) == gpio.HIGH:
		return True
	else:
		return False


def stop_condition():
	if gpio.input(configuration['top_switch']) == gpio.HIGH or gpio.input(configuration['bottom_switch']) == gpio.HIGH:
		return False
	else:
		return True


def run_program():
	setup()
	while True:
		while stop_condition():
			motor_rotate()
		break
