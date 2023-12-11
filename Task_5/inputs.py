#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, SpeedPercent
from math import sin, cos
import time

# Создаем объект двигателя
motor = LargeMotor(OUTPUT_A)

# Коэффициенты для входных воздействий
A1, A2, A3 = 10, 20, 30
w1, w2, w3 = 0.5, 1.0, 1.5

# Время начала
start_time = time.time()

motor_data = [{
    "angle": 0,
    "speed": 0,
    "time": 0
}]
t = 0

while True and t < 5:
    # Текущее время
    t = time.time() - start_time

    # Расчет входных воздействий
    input1 = A1 * sin(w1 * t)
    input2 = A2 * cos(w2 * t) + A3 * sin(w3 * t)

    # Подаем воздействие на двигатель
    motor.on(SpeedPercent(input1))

    current_angle = motor.position

    # Получаем текущую угловую скорость мотора
    current_speed = motor.speed
    motor_data.append({
        "angle": current_angle,
        "speed": current_speed,
        "time": t
    })

motor.stop()
print(motor_data)
