from library.camera_tray.camera_rotation import setup as camera_rotation, cleanup as camera_rotation_clean
# from library.main_tray.tray_down import setup as tray_down, cleanup as tray_down_clean
# from library.main_tray.tray_up import setup as tray_up, cleanup as tray_up_clean
import RPi.GPIO as gpio
import json

config_file = open("config.json", 'r')
configuration = json.loads(config_file.read())

while True:
	camera_rotation()
	# tray_down()
	# tray_up()
	
	# #tray switch
	# if gpio.input(configuration['tray']['top_switch']) == gpio.HIGH or gpio.input(configuration['tray']['top_switch']) == gpio.HIGH:
	# 	tray_down_clean()
	# 	tray_up_clean()
	
	# camera switch
	if gpio.input(configuration['camera_tray']['switch']) == gpio.HIGH:
		camera_rotation_clean()
