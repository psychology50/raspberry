#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

#define SWITCH_DEVICE "/dev/SWITCH_DRIVER"

int main() {
    int switch_dev;
    int switch_state;

    // 디바이스 파일을 엽니다.
    switch_dev = open(SWITCH_DEVICE, O_RDONLY);
    if (switch_dev < 0) {
        perror("Failed to open the device");
        return 1;
    }

    // 스위치의 상태를 읽습니다.
    if (read(switch_dev, &switch_state, sizeof(switch_state)) < 0) {
        perror("Failed to read the device");
        return 1;
    }

    printf("The switch state is: %d\n", switch_state);

    // 디바이스 파일을 닫습니다.
    close(switch_dev);

    return 0;
}
