cmd_/root/raspberry/iot/key_driver/key_driver.mod := printf '%s\n'   key_driver.o | awk '!x[$$0]++ { print("/root/raspberry/iot/key_driver/"$$0) }' > /root/raspberry/iot/key_driver/key_driver.mod
