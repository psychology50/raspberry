cmd_/root/raspberry/iot/test_buzzer/buzzer_driver.mod := printf '%s\n'   buzzer_driver.o | awk '!x[$$0]++ { print("/root/raspberry/iot/test_buzzer/"$$0) }' > /root/raspberry/iot/test_buzzer/buzzer_driver.mod
