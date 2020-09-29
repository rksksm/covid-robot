from flask import Flask, render_template, jsonify, request
from library.main_tray.tray_up import run_program as tray_up
from library.main_tray.tray_down import run_program as tray_down
from library.camera_tray.camera_rotation import run_program as camera_tray
from library.medicine_tray.medicine_tray import run_program as medicine_tray
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

current_tray_position = 1
medicine_tray_angle = 248.1

@app.route('/')
def home():
	return render_template("index.html")


@app.route('/power')
def power():
	status = request.args.get('status')
	if status == 'true':
		tray_up()
		return jsonify({"message": "Powered on successfully"})
	elif status == 'false':
		tray_down()
		return jsonify({"message": "Powered off successfully"})
	else:
		pass


@app.route('/medicine')
def medicine():
	global current_tray_position
	tray_id = int(request.args.get('tray_id'))
	if tray_id == current_tray_position:
		return jsonify({"message": "tray on same position"})
	elif tray_id < current_tray_position:
		steps = (current_tray_position - tray_id) * medicine_tray_angle
		current_tray_position = tray_id
		medicine_tray(steps=steps, direction='backward')
		return jsonify({"message": "tray rotated successfully"})
	elif tray_id > current_tray_position:
		steps = (tray_id - current_tray_position) * medicine_tray_angle
		current_tray_position = tray_id
		medicine_tray(steps=steps, direction='forward')
		return jsonify({"message": "tray rotated successfully"})


@app.route('/camera')
def camera():
	direction = request.args.get('direction')
	if direction == 'left':
		camera_tray(direction='backward')
		return jsonify({"message": "tray rotated successfully"})
	if direction == 'right':
		camera_tray(direction='forward')
	return jsonify({"message": "tray rotated successfully"})


if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', port=5000, debug=True)
	except KeyboardInterrupt:
		GPIO.cleanup()
