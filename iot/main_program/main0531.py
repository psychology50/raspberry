import time
import board
import adafruit_dht
import threading
import I2C_LCD_driver
import os
import struct 
from fire_danger_index import calculate_fire_danger_index
import requests


mylcd=I2C_LCD_driver.lcd()

dhtDevice = adafruit_dht.DHT11(board.D5)
dhtDevice2= adafruit_dht.DHT11(board.D6)

led_file="/dev/led_driver"
buzzer_device="/dev/buzzer_driver"

switch_device = "/dev/switch_driver" # 스위치 디바이스 파일을 설정합니다.
# 전역변수 정의
global_temperature1 = 0
global_humidity1 = 0
global_temperature2 = 0
global_humidity2 = 0

global_fire_danger1="Green"
global_fire_danger2="Green"
# 뮤텍스 객체 생성. 위험지수에 사용
mutex1 = threading.Lock()
mutex2 = threading.Lock()

def send_data_to_flask(spot,temperature, humidity):
	data = {'spot':spot,'temperature': temperature, 'humidity': humidity}  # 전송할 데이터
	flask_url = 'http://localhost:8080/send-mail'
	response = requests.post(flask_url, json=data)  # POST 요청 보내기

	if response.status_code == 200:
		print('Data sent to Flask server successfully')
	else:
		print('Failed to send data to Flask server')



# 스위치 값을 읽는 함수입니다.
def read_switch():
	try:
		with open(switch_device, 'rb') as switch_dev:
			data = switch_dev.read(4)
			value = struct.unpack('I', data)[0]
			print("switch",value)
			return value
	except IOError as e:
		print(f"Failed to open the switch device: {e}")
	return None




def buzzer():
# 디바이스 파일을 연다.
	try:
		buzzer_dev = os.open(buzzer_device, os.O_WRONLY)	
		while True:        
			time.sleep(1.0)
			mutex1.acquire()
			fire_hazard_index1 = global_fire_danger1
			mutex1.release()

			mutex2.acquire()
			fire_hazard_index2= global_fire_danger2
			mutex2.release()

			# 스위치 값이 변경될 때까지 계속 읽는다.
			switch_value = read_switch()
            # 스위치가 눌리면 부저를 꺼야 합니다.
			if switch_value == 1:
				break
			if fire_hazard_index1 == "Red" or fire_hazard_index2 == "Red":
                # 주파수 값을 설정한다.
				frequency = 1000  # 예시로 1000Hz로 설정

                # 주파수 값을 바이트 형식으로 변환한다.
				frequency_bytes = struct.pack('I', frequency)

                # 디바이스에 주파수 값을 쓴다.
				os.write(buzzer_dev, frequency_bytes)

                # 2초간 sleep
				time.sleep(2)
	except OSError as e:
		print(f"Failed to open the device: {e}")
	finally:
		if buzzer_dev:
			os.close(buzzer_dev)

def led():
	try:
		fd = os.open(led_file, os.O_RDWR)
		while True:
			time.sleep(1.0)	
			mutex1.acquire()
			fire_hazard_index1=global_fire_danger1
			mutex1.release()

			mutex2.acquire()
			fire_hazard_index2=global_fire_danger2
			mutex2.release()

			if fire_hazard_index1 == "Red" or fire_hazard_index2 =="Red":
				os.write(fd,bytes([0x03]))
			elif fire_hazard_index1 =="Yellow" or fire_hazard_index2 == "Yellow":
				os.write(fd,bytes([0x02]))
			else:
				os.write(fd,bytes([0x01]))
				
	except OSError as e:
		print(f"Error: {e}")
#	finally:
#		 if fd:
#os.close(fd)

def LCD():
	while True:
		try:
			time.sleep(1.0)
			mutex1.acquire()
			temperature_c1 = global_temperature1
			humidity1 = global_humidity1
			mutex1.release()

			
			mylcd.lcd_display_string("DHT1:{:.1f}C/H:{:.1f}%".format(temperature_c1,humidity1), 1)
            
			mutex2.acquire()
			temperature_c2 = global_temperature2
			humidity2 = global_humidity2
			mutex2.release()
			
			mylcd.lcd_display_string("DHT2:{:.1f}C/H:{:.1f}".format(temperature_c2,humidity2), 2)
#           mylcd.lcd_display_string("Humidity: {}%".format(humidity2), 4)
		except KeyboardInterrupt:
			pass
		


def dht1():
	global global_temperature1
	global global_humidity1
	global global_fire_danger1
	send_flag=False
	while True:
		try:
			temperature_c = dhtDevice.temperature
			temperature_f = temperature_c *(9/5) + 32
			humidity = dhtDevice.humidity
			print("DHT1 Temp: {:.1f} F / {:.1f}C  Humidity: {}% ".format(temperature_f, temperature_c, humidity))
			fire_danger_index1 = calculate_fire_danger_index(temperature_c,humidity)
			# 전역변수에 측정값 저장
			mutex1.acquire()
			
			global_temperature1 = temperature_c
			global_humidity1 = humidity
			global_fire_danger1=fire_danger_index1
			
			mutex1.release()
			if 	fire_danger_index1 == "Red" and send_flag==False:
				send_data_to_flask("DHT1",temperature_c,humidity)
				send_flag=True

			time.sleep(1.0)
		except KeyboardInterrupt:
			print('Exit with ^C')
			exit()

def dht2():
	global global_temperature2
	global global_humidity2
	global global_fire_danger2
	send_flag=False
	while True:
		try:
			temperature_c = dhtDevice2.temperature
			temperature_f = temperature_c*(9/5)+32
			humidity=dhtDevice2.humidity
			print("DHT2 Temp:{:.1f} F / {:.1f}C Humidity: {}% ".format(temperature_f, temperature_c, humidity))
			# 전역변수에 측정값 저장
			fire_danger_index2 = calculate_fire_danger_index(temperature_c,humidity)
			mutex2.acquire()
			global_temperature2 = temperature_c
			global_humidity2 = humidity
			global_fire_danger2= fire_danger_index2
			mutex2.release()
		
			if fire_danger_index2 == "Red" and send_flag==False:
				send_data_to_flask("DHT2",temperature_c,humidity)
				send_flag=True
			time.sleep(1.0)
		except KeyboardInterrupt:
			print('Exit with ^C')
			exit()

thread1 = threading.Thread(target=dht1)
thread1.start()
thread2 = threading.Thread(target=dht2)
thread2.start()

thread_lcd = threading.Thread(target=LCD)
thread_lcd.start()

thread_led = threading.Thread(target=led)
thread_led.start()

thread_buzzer = threading.Thread(target=buzzer)
thread_buzzer.start()
