#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, SpeedPercent
import time

import json

motor = LargeMotor(OUTPUT_A)

Kp = 1.0
target_angle = 90


# Функция П-регулятора
def P_control(Kp, error):
    return Kp * error


def limit(value):
    if value > 100:
        return 100
    if value < -100:
        return -100
    return value


def dict_to_json(dict_data, filename):
    with open(filename, 'w') as f:
        json.dump(dict_data, f)


if __name__ == '__main__':
    start_time = time.time()
    current_time = 0
    data = [{
        "angle": 0,
        "time": 0
    }]

    while True and current_time < 10:
        current_angle = motor.position
        current_time = time.time() - start_time
        error = target_angle - current_angle
        control = limit(P_control(Kp, error))
        motor.on(SpeedPercent(control))
        pos_data = {
            "angle": current_angle,
            "time": current_time
        }
        data.append(pos_data)
        # if abs(error) < 0.5:
        #     motor.stop()
        #     break

        time.sleep(0)
    motor.stop()
    print(data)
    dict_to_json(data, 'data.json')