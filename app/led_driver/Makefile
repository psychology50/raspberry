MODULE_NAME=led_driver
APP_NAME=test_led
KDIR = /lib/modules/`uname -r`/build
TOOLCHAIN=arm-linux-gnueabihfCC=$(TOOLCHAIN)gcc
TARGET=arm
obj-m := $(MODULE_NAME).o
all: app driver
driver:
	$(MAKE) -C $(KDIR) M=$$PWD modules
app:
	$(CC) -o $(APP_NAME) $(APP_NAME).c
clean:
	$(MAKE) -C $(KDIR) M=$$PWD clean
