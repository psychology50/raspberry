def calculate_fire_danger_index(temperature, relative_humidity):
    if temperature >= 30 and relative_humidity < 100: #원래:35도이상,습도25
        return "Red"  # 온도 35도 이상, 상대습도 25% 미만: 매우 높음 등급
    elif temperature >= 27 and relative_humidity < 100: #원래: 28도이상, 습도60
        return "Yellow"  # 온도 28도 이상, 상대습도 40% 미만: 높음 등급
    else:
        return "Green"  # 나머지 경우: 보통 등급

