import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

# Initialise I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, 16, 2)

# Clear the LCD screen
lcd.clear()

# Set LCD color to red
lcd.color = [100, 0, 0]

# Print message
lcd.message = "Hello, World!"

# Wait for 5 seconds
time.sleep(5)

# Clear the LCD screen and turn off the backlight
lcd.clear()
lcd.color = [0, 0, 0]

