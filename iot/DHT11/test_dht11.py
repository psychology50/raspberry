#sudo pip3 install Adafruit_DHT 라이브러리 설치 후 사용

import Adafruit_DHT

# DHT11 센서를 지정합니다.
DHT_SENSOR = Adafruit_DHT.DHT11

# 센서가 연결된 GPIO 핀을 지정합니다. 여기서는 4번 핀을 사용했습니다.
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.")