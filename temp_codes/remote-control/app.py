from flask import Flask, render_template
# import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)


@app.route('/')
def home():
	return render_template("index.html")


@app.route('/led_on')
def led_on():
	GPIO.output(18, GPIO.HIGH)
	return "LED on"


@app.route('/led_off')
def led_off():
	GPIO.output(18, GPIO.LOW)
	return "LED off"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
