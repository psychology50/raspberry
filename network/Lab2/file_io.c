#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>


int main(void)
{

	int fd, fd1;
	char buf[]="Computer Network 2023 ZZANG!\n";
	char read_buf[1024];
	int read_len=0;

	fd=open("data.txt", O_CREAT|O_WRONLY|O_TRUNC);

	printf("file descritor: %d\n",fd);

	write(fd, buf, sizeof(buf));

	fd1=open("read_data_file.txt",O_RDONLY);

	read_len=read(fd1,read_buf,sizeof(read_buf));

	printf("Read result: %s, Read length: %d\n",read_buf,read_len);

	close(fd);
	close(fd1);

	return 0;
}

