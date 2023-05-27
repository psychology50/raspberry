import time
import board
import adafruit_dht
import threading

dhtDevice = adafruit_dht.DHT11(board.D5)
dhtDevice2= adafruit_dht.DHT11(board.D6)

def dht1():
	while True:
		try:
			temperature_c = dhtDevice.temperature
			temperature_f = temperature_c *(9/5) + 32
			humidity = dhtDevice.humidity
			print("DHT1 Temp: {:.1f} F / {:.1f}C  Humidity: {}% ".format(temperature_f, temperature_c, humidity))
			time.sleep(2.0)
		except KeyboardInterrupt:
			pass
			print('Exit with ^C')
			exit()

def dht2():
	while True:
		try:
			temperature_c = dhtDevice2.temperature
			temperature_f = temperature_c*(9/5)+32
			humidity=dhtDevice2.humidity
			print("DHT2 Temp:{:.1f} F / {:.1f}C Humidity: {}% ".format(temperature_f, temperature_c, humidity))
			time.sleep(2.0)
		except KeyboardInterrupt:
			pass
			print('Exit with ^C')
			exit()

thread1 = threading.Thread(target=dht1())
thread1.start()
thread2 = threading.Thread(target=dht2())
thread2.start()
