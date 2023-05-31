def calculate_fire_danger_index(temperature, relative_humidity):
    if temperature >= 35 and relative_humidity < 25:
        return "Red"  # 온도 35도 이상, 상대습도 25% 미만: 매우 높음 등급
    elif temperature >= 28 and relative_humidity < 40:
        return "Yellow"  # 온도 28도 이상, 상대습도 40% 미만: 높음 등급
    else:
        return "Green"  # 나머지 경우: 보통 등급

