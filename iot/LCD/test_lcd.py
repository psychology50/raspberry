#python3 -m pip install smbus

import smbus
import time

# I2C LCD 주소
LCD_ADDRESS = 0x27

# I2C 버스 초기화
bus = smbus.SMBus(1)

# LCD 초기화 및 설정 명령어
LCD_CMD = 0x00
LCD_CHR = 0x40
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0
LCD_BACKLIGHT = 0x08
ENABLE_BIT = 0x04

# 초기화 함수
def lcd_init():
    lcd_byte(0x33, LCD_CMD)  # 4-bit 모드 초기화
    lcd_byte(0x32, LCD_CMD)  # 4-bit 모드 초기화
    lcd_byte(0x28, LCD_CMD)  # 2줄 디스플레이, 5x8 폰트
    lcd_byte(0x0C, LCD_CMD)  # 디스플레이 On, 커서 Off
    lcd_byte(0x06, LCD_CMD)  # 커서 이동 방향 설정

# 문자 출력 함수
def lcd_byte(bits, mode=LCD_CHR):
    bus.write_byte(LCD_ADDRESS, bits | LCD_BACKLIGHT)
    lcd_toggle_enable(bits | LCD_BACKLIGHT)

# Enable 토글 함수
def lcd_toggle_enable(bits):
    time.sleep(0.0005)
    bus.write_byte(LCD_ADDRESS, (bits | ENABLE_BIT))
    time.sleep(0.0005)
    bus.write_byte(LCD_ADDRESS, (bits & ~ENABLE_BIT))
    time.sleep(0.0005)

# 문자열 출력 함수
def lcd_string(message, line):
    message = message.ljust(16, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(16):
        lcd_byte(ord(message[i]), LCD_CHR)

try:
    # I2C LCD 초기화
    lcd_init()

    while True:
        # Do something
        # 첫 번째 줄에 문자열 출력
        lcd_string("Hello, World!", LCD_LINE_1)
        # 두 번째 줄에 시간 출력
        lcd_string(time.strftime("%H:%M:%S"), LCD_LINE_2)
        time.sleep(1)

except KeyboardInterrupt:
    pass

# GPIO 설정 초기화
GPIO.cleanup()
