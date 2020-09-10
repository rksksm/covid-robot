from time import sleep
import RPi.GPIO as gpio
import json

config_file = open("../../config.json", 'r')
configuration = json.loads(config_file.read())["tray"]
print(configuration)

motor_moving = False

direction = 1

def setup():
	# setting up the Respberry pi modes
	gpio.setwarnings(False)  # Ignore warning for now
	gpio.setmode(gpio.BCM)  # Use physical pin numbering

	# setting up the motor 1
	gpio.setup(configuration['motor_1_direction_pin'], gpio.OUT)
	gpio.setup(configuration['motor_1_step_pin'], gpio.OUT)
	gpio.output(configuration['motor_1_direction_pin'], direction)

	# setting up the motor 2
	gpio.setup(configuration['motor_2_direction_pin'], gpio.OUT)
	gpio.setup(configuration['motor_2_step_pin'], gpio.OUT)
	gpio.output(configuration['motor_2_direction_pin'], direction)

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
	if gpio.input(configuration['top_switch']) == gpio.HIGH and gpio.input(configuration['bottom_switch']) == gpio.LOW:
		return False
	else:
		return True


if __name__ == '__main__':
	setup()
	print("setup completed")
	while True:
		print("entered main program")
		while start_condition():
			print("condition 1 success")
			while stop_condition():
				print("condition 2 success")
				motor_rotate()
			print("condition 2 failed")
		print("condition 1 failed")
