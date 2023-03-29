CC = gcc
OBJS = hello.o main.o
TARGET = hello_make2
$(TARGET): $(OBJS)
	$(CC) -o $@ $^
install:
	cp $(TARGET) /usr/bin
clean: 
	rm $(TARGET) $(OBJS)
