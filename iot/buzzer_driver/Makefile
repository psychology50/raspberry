MODULE_NAME = buzzer_driver
APP_NAME = test_buzzer
KDIR = /lib/modules/`uname -r`/build
TARGET = arm

obj-m := $(MODULE_NAME).o
all: app driver
driver:
	$(MAKE) -C $(KDIR) SUBDIRS=$(PWD) ARCH=$(TARGET) M=$$PWD modules
app:
	$(CC) -o $(APP_NAME) $(APP_NAME).c
clean:
	$(MAKE) -C $(KDIR) M=$$PWD clean

