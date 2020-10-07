from time import sleep
import RPi.GPIO as gpio
import json

config_file = open("../../config.json", 'r')
configuration = json.loads(config_file.read())["bldc"]
print(configuration)

motor_moving = False
direction = 1


def setup():
	# setting up the RaspberryPi modes
	gpio.setwarnings(False)  # Ignore warning for now
	gpio.setmode(gpio.BCM)  # Use physical pin numbering

	# setting up the motor 1
	gpio.setup(configuration['PWM1'], gpio.OUT)
	gpio.setup(configuration['startStop1'], gpio.OUT)
	gpio.setup(configuration['Direction1'], gpio.OUT)

	# setting up the motor 1
	gpio.setup(configuration['PWM2'], gpio.OUT)
	gpio.setup(configuration['startStop2'], gpio.OUT)
	gpio.setup(configuration['Direction2'], gpio.OUT)

	pi_pwm1 = gpio.PWM(configuration['PWM1'], 1000)  # create PWM instance with frequency
	pi_pwm1.start(50)

	pi_pwm2 = gpio.PWM(configuration['PWM2'], 1000)  # create PWM instance with frequency
	pi_pwm2.start(50)
	gpio.output(configuration['startStop1'], gpio.LOW)
	gpio.output(configuration['startStop2'], gpio.LOW)
	return pi_pwm1, pi_pwm2

def cleanup():
	gpio.cleanup()


def move_forward(pwm1, pwm2):
	gpio.output(configuration['Direction1'], gpio.LOW)
	gpio.output(configuration['Direction2'], gpio.LOW)
	pwm1.ChangeDutyCycle(55)
	pwm2.ChangeDutyCycle(55)


def move_backward(pwm1, pwm2):
	gpio.output(configuration['Direction1'], gpio.HIGH)
	gpio.output(configuration['Direction2'], gpio.HIGH)
	pwm1.ChangeDutyCycle(55)
	pwm2.ChangeDutyCycle(55)


def move_left(pwm1, pwm2):
	gpio.output(configuration['Direction1'], gpio.LOW)
	gpio.output(configuration['Direction2'], gpio.HIGH)
	pwm1.ChangeDutyCycle(55)
	pwm2.ChangeDutyCycle(55)


def move_right(pwm1, pwm2):
	gpio.output(configuration['Direction1'], gpio.HIGH)
	gpio.output(configuration['Direction2'], gpio.LOW)
	pwm1.ChangeDutyCycle(55)
	pwm2.ChangeDutyCycle(55)


def stop():
	gpio.output(configuration['startStop1'], gpio.HIGH)
	gpio.output(configuration['startStop2'], gpio.HIGH)


def run_program(direction=None):
	pwm1, pwm2 = setup()
	print("setup completed")
	if direction == 'left':
		move_left(pwm1, pwm2)
	if direction == 'right':
		move_right(pwm1, pwm2)
	if direction == 'forward':
		move_forward(pwm1, pwm2)
	if direction == 'backward':
		move_backward(pwm1, pwm2)
	if direction == 'stop':
		stop()
