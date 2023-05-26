MODULE_NAME = key_driver
APP_NAME = test_key
KDIR = /lib/modules/`uname -r`/build
TARGET = arm

obj-m := $(MODULE_NAME).o
all: app driver
driver:
	$(MAKE) -C $(KDIR) M=$$PWD modules
app:
	$(CC) -o $(APP_NAME) $(APP_NAME).c
clean:
	$(MAKE) -C $(KDIR) M=$$PWD clean

