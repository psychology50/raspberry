import os
import time
import RPi.GPIO as GPIO

LED_DEVICE = "/dev/led_driver"
SWITCH_DEVICE = "/dev/switch_driver"

BUZZER_PIN = 23
FREQUENCY = 440

def device_control():
	try:
		# open led device file
		led_fd = os.open(LED_DEVICE, os.O_RDWR)
		switch_fd = os.open(SWITCH_DEVICE, os.O_RDONLY)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(BUZZER_PIN, GPIO.OUT)
		pwm = GPIO.PWM(BUZZER_PIN, FREQUENCY)

		if led_fd < 0 or switch_fd < 0:
			print(f"Can't open: {LED_DEVICE}")
			exit(1)

		while True:
			switch_state = os.read(switch_fd, 4)
			switch_state = int.from_bytes(switch_state, byteorder="little")

			print(f"The switch state is : {switch_state}")
			
			flag = 0
			if switch_state:
				if not flag:
					pwm.start(80)
					flag = 1
				os.write(led_fd, bytes([10]))
			else:
				flag = 0
				os.write(led_fd, bytes([1]))
				pwm.stop()		

			time.sleep(1)
	except OSError as e:
		print("OS Error : ", e)
device_control()
