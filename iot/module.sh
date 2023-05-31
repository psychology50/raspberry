rm -rf /dev/led_driver
rm -rf /dev/switch_driver
rm -rf /dev/buzzer_driver

rmmod led_driver
rmmod switch_driver
rmmod buzzer_driver

mknod /dev/led_driver c 221 0
mknod /dev/switch_driver c 222 0
mknod /dev/buzzer_driver c 100 0

insmod ./led_driver/led_driver.ko
insmod ./switch_driver/switch_driver.ko
insmod ./buzzer_driver/buzzer_driver.ko
