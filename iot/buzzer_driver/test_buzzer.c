#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

#define BUZZER_DEVICE "/dev/BUZZER_DRIVER"

int main() {
    int buzzer_dev;
    char state;

    // 디바이스 파일을 엽니다.
    buzzer_dev = open(BUZZER_DEVICE, O_WRONLY);
    if (buzzer_dev < 0) {
        perror("Failed to open the device");
        return 1;
    }

    // 버저를 켭니다.
    state = 1;
    if (write(buzzer_dev, &state, sizeof(state)) < 0) {
        perror("Failed to write the device");
        return 1;
    }

    sleep(2); // 2초 동안 버저를 울립니다.

    // 버저를 끕니다.
    state = 0;
    if (write(buzzer_dev, &state, sizeof(state)) < 0) {
        perror("Failed to write the device");
        return 1;
    }

    // 디바이스 파일을 닫습니다.
    close(buzzer_dev);

    return 0;
}
