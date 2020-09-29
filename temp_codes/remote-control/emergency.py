import RPi.GPIO as gpio
import json

config_file = open("config.json", 'r')
configuration = json.loads(config_file.read())
print(configuration)

def setup():
	# setting up the RaspberryPi modes
	gpio.setwarnings(False)  # Ignore warning for now
	gpio.setmode(gpio.BCM)  # Use physical pin numbering
	
	# setting up the motor
	gpio.setup(configuration['motor_in1'], gpio.OUT)
	gpio.setup(configuration['motor_in2'], gpio.OUT)
	
	# setting up cut switches
	gpio.setup(configuration['switch'], gpio.IN, pull_up_down=gpio.PUD_DOWN)  # switch

setup_flag = False
while True:
	if not setup_flag:
		setup()
		setup_flag = True
	
	if gpio.input(configuration['camera_tray']['switch']) == gpio.HIGH:
		gpio.cleanup()
		setup_flag = False
