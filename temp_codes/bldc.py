import RPi.GPIO as gpio
from time import sleep
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
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

# while True:
# 	for i in range(0, 100, 5):
# 		pi_pwm1.ChangeDutyCycle(i)
# 		sleep(1)
# 		print(i)


@app.route('/bldc')
def bldc_move():
	command = request.args.get('instruction')
	if command == 'forward':
		while True:
			pi_pwm1.ChangeDutyCycle(100)
	elif command == 'backward':
		print(command)
	elif command == 'left':
		print(command)
	elif command == 'right':
		print(command)
	elif command == 'stop':
		while True:
			pi_pwm1.ChangeDutyCycle(0)
	else:
		print("nothing")
	return command

if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', port=5000, debug=True)
	except KeyboardInterrupt:
		GPIO.cleanup()
