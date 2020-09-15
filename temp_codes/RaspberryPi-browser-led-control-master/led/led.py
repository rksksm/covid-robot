from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)


# {{url}}/led?status=on
@app.route('/', methods=['GET'])
def led():
	status = request.args.get('status')
	if status == "on":
		GPIO.output(18, GPIO.HIGH)
		return jsonify({"message": "Led successfully turned on"})
	elif status == "off":
		GPIO.output(18, GPIO.LOW)
		return jsonify({"message": "Led successfully turned off"})
	else:
		return jsonify({"message": "Not a valid status"})


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
