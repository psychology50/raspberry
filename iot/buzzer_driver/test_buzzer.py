import RPi.GPIO as GPIO
import time

BUZZER_PIN = 23
FREQUENCY = 440  # Hz

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Setup the buzzer pin for output
GPIO.setup(BUZZER_PIN, GPIO.OUT)

try:
    # Create a PWM instance
    pwm = GPIO.PWM(BUZZER_PIN, FREQUENCY)

    # Start the PWM signal
    pwm.start(50)  # 50 is the duty cycle, change as per your requirement

    # Keep the buzzer on for some time
    time.sleep(1)

finally:
    # Stop the PWM signal
    pwm.stop()

    # Cleanup the GPIOs
    GPIO.cleanup()

