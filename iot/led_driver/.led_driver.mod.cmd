cmd_/root/raspberry/iot/led_driver/led_driver.mod := printf '%s\n'   led_driver.o | awk '!x[$$0]++ { print("/root/raspberry/iot/led_driver/"$$0) }' > /root/raspberry/iot/led_driver/led_driver.mod
