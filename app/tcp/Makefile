CC = gcc
OBJ1 = server.o
OBJ2 = client.o
TARGET1 = server_host
TARGET2 = client_host
all: $(TARGET1) $(TARGET2)
$(TARGET1): $(OBJ1)
	$(CC) -o $@ $^
$(TARGET2): $(OBJ2)
	$(CC) -o $@ $^
clean:
	rm $(TARGET1) $(TARGET2)
	rm $(OBJ1) $(OBJ2)
