import os
import time

LED_DEVICE = "/dev/led_driver"
SWITCH_DEVICE = "/dev/switch_driver"

def device_control():
	try:
		# open led device file
		led_fd = os.open(LED_DEVICE, os.O_RDWR)
		switch_fd = os.open(SWITCH_DEVICE, os.O_RDONLY)
		
		if led_fd < 0 or switch_fd < 0:
			print(f"Can't open: {LED_DEVICE}")
			exit(1)

		while True:
			switch_state = os.read(switch_fd, 4)
			switch_state = int.from_bytes(switch_state, byteorder="little")

			print(f"The switch state is : {switch_state}")

			if switch_state:
				os.write(led_fd, bytes([10]))
			else:
				os.write(led_fd, bytes([1]))
			time.sleep(1)
	except OSError as e:
		print("OS Error : ", e)

