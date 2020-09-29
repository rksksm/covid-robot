from time import sleep
import RPi.GPIO as gpio
import json

config_file = open("../../config.json", 'r')
configuration = json.loads(config_file.read())["camera_tray"]
print(configuration)

motor_moving = False


def setup():
	# setting up the RaspberryPi modes
	gpio.setwarnings(False)  # Ignore warning for now
	gpio.setmode(gpio.BCM)  # Use physical pin numbering
	# setting up the motor
	gpio.setup(configuration['motor_in1'], gpio.OUT)
	gpio.setup(configuration['motor_in2'], gpio.OUT)
	# gpio.setup(configuration['motor_ena'], gpio.OUT)
	gpio.output(configuration['motor_in1'], gpio.LOW)
	gpio.output(configuration['motor_in2'], gpio.LOW)
	# motorSpeed = gpio.PWM(configuration['motor_ena'], 1000)
	# motorSpeed.start(100)
	# setting up cut switches
	gpio.setup(configuration['switch'], gpio.IN, pull_up_down=gpio.PUD_DOWN)  # switch


def motor_rotate_forward():
	gpio.output(configuration['motor_in1'], gpio.HIGH)
	gpio.output(configuration['motor_in2'], gpio.LOW)


def motor_rotate_backward():
	gpio.output(configuration['motor_in1'], gpio.LOW)
	gpio.output(configuration['motor_in2'], gpio.HIGH)


def motor_stop():
	gpio.output(configuration['motor_in1'], gpio.LOW)
	gpio.output(configuration['motor_in2'], gpio.LOW)


def stop_condition():
	if gpio.input(configuration['switch']) == gpio.HIGH:
		return True


def cleanup():
	gpio.cleanup()


def run_program(direction):
	setup()
	print("setup completed")
	if direction == 'forward':
		print('right')
		motor_rotate_forward()
	if direction == 'backward':
		print('left')
		motor_rotate_backward()
	if direction == 'stop':
		motor_stop()
	if gpio.input(configuration['switch']) == gpio.HIGH:
		motor_stop()
