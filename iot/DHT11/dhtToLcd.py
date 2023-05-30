import time
import board
import adafruit_dht
import threading
import I2C_LCD_driver

mylcd=I2C_LCD_driver.lcd()

dhtDevice = adafruit_dht.DHT11(board.D5)
dhtDevice2= adafruit_dht.DHT11(board.D6)


def LCD():
    while True:
        try:
            time.sleep(2.0)
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9/5) + 32
            humidity = dhtDevice.humidity
            mylcd.lcd_display_string("DHT1:{:.1f}C/H:{:.1f}%".format(temperature_c,humidity), 1)
#mylcd.lcd_display_string("Humidity: {}%".format(humidity), 2)
            
            temperature_c2 = dhtDevice2.temperature
            temperature_f2 = temperature_c2 * (9/5) + 32
            humidity2 = dhtDevice2.humidity
            mylcd.lcd_display_string("DHT2:{:.1f}C/H:{:.1f}".format(temperature_c2,humidity2), 2)
#           mylcd.lcd_display_string("Humidity: {}%".format(humidity2), 4)
            
            time.sleep(0.1)
        except KeyboardInterrupt:
            pass
		


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

thread1 = threading.Thread(target=dht1)
thread1.start()
thread2 = threading.Thread(target=dht2)
thread2.start()

thread_lcd = threading.Thread(target=LCD)
thread_lcd.start()
