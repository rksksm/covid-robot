from time import sleep
import RPi.GPIO as gpio
import json

config_file = open("../../config.json", 'r')
configuration = json.loads(config_file.read())["bldc"]
print(configuration)

motor_moving = False
pi_pwm = None
direction = 1


def setup():
	# setting up the RaspberryPi modes
	gpio.setwarnings(False)  # Ignore warning for now
	gpio.setmode(gpio.BCM)  # Use physical pin numbering

	# setting up the motor 1
	gpio.setup(configuration['PWM1'], gpio.OUT)
	gpio.setup(configuration['ground1'], gpio.OUT)
	gpio.setup(configuration['ground2'], gpio.OUT)

	pi_pwm = gpio.PWM(configuration['PWM1'], 1000)  # create PWM instance with frequency
	pi_pwm.start(10)


def cleanup():
	gpio.cleanup()

if __name__ == '__main__':
	setup()
	print("setup completed")
	while True:
		pi_pwm.ChangeDutyCycle(50)
		gpio.output(37, gpio.LOW)
