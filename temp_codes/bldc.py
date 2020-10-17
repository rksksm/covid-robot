import RPi.GPIO as gpio
from time import sleep

configuration = {
	"PWM1": 12,
	"startStop1": 1,
	"Direction1": 26,
	"PWM2": 13,
	"startStop2": 0,
	"Direction2": 4
}

gpio.setwarnings(False)  # Ignore warning for now
gpio.setmode(gpio.BCM)  # Use physical pin numbering

# setting up the motor 1
gpio.setup(configuration['PWM1'], gpio.OUT)
gpio.setup(configuration['startStop1'], gpio.OUT)
gpio.setup(configuration['Direction1'], gpio.OUT)
pi_pwm1 = gpio.PWM(configuration['PWM1'], 1000)
pi_pwm1.start(20)

while true:
	pi_pwm1.ChangeDutyCycle(55)
