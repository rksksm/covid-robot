import RPi.GPIO as GPIO
import time

sensor = 5
buzzer = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)

try:
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,True)
          print("Object Detected")
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(buzzer,False)


except KeyboardInterrupt:
    GPIO.cleanup()