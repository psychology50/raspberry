import lirc

# 리모컨 설정 파일 경로
config_file = "/etc/lirc/lircd.conf"

# 리모컨 신호 수신 함수
def receive_remote_signal():
    sockid = lirc.init("myprogram", config_file)
    while True:
        code = lirc.nextcode()
        if code:
            # 수신된 신호 처리
            print("Received signal:", code[0])

try:
    # 리모컨 신호 수신 시작
    receive_remote_signal()

except KeyboardInterrupt:
    pass

# 리모컨 초기화
lirc.deinit()
