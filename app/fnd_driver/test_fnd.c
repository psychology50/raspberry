#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <linux/kdev_t.h>
#define KEY_FILE_NAME "/dev/fnd_driver"

int main(int argc, char **argv) {
	int fnd_fd;
	char data;
	int number;
	char fnd_values[13] = {
		0xFC, 0x60, 0xDA, 0xF2, // 0, 1, 2, 3
		0x66, 0xB6, 0xBE, 0xE4, // 4, 5, 6, 7
		0xFE, 0xF6, 0x01, 0xFF, // 8, 9, DP, All
		0x00					// Off
	}

	fnd_fd = open(FND_FILE_NAME, O_RDWR);
	if (fnd_fd < 0) {
		fprintf(stderr, "Cant't open %s\n", FND_FILE_NAME);
		return -1;
	}
	while (1) {
		printf("[app] input number : ");
		scanf("%d", &number);
		if (number < 0 || number > 12)
			fprintf(stderr, "Invalid value, TRy again(0~12).\n");
		else
			write(fnd_fd, &fnd_values[number], sizeof(char));
	}
	close(fnd_fd);

	return 0;
}
