#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

#define BUZZER_DEVICE "/dev/buzzer_driver"

int main() {
    int buzzer_dev;
    unsigned int frequency;

    // 디바이스 파일을 엽니다.
    buzzer_dev = open(BUZZER_DEVICE, O_WRONLY);
    if (buzzer_dev < 0) {
        perror("Failed to open the device");
        return 1;
    }

    // 주파수 값을 설정합니다.
    frequency = 1000; // 예시로 1000Hz로 설정

    // 주파수 값을 디바이스에 쓰기 위해 state에 저장합니다.
    char state[sizeof(frequency)];
    memcpy(state, &frequency, sizeof(frequency));
while(1){
    // 디바이스에 주파수 값을 씁니다.
    if (write(buzzer_dev, state, sizeof(state)) < 0) {
        perror("Failed to write the device");
        return 1;
    }
	sleep(2);
}
    close(buzzer_dev);

    return 0;
}
