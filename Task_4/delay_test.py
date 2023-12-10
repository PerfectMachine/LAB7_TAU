from ev3dev2.motor import LargeMotor, OUTPUT_A, SpeedPercent
import time

# Создаем объект двигателя
motor = LargeMotor(OUTPUT_A)

# Параметры П-регулятора
Kp = 1.0
target_angle = 90  # Целевой угол в градусах

# Функция П-регулятора
def P_control(Kp, error):
    return Kp * error

# Основной цикл управления
while True:
    current_angle = motor.position  # Текущий угол
    error = target_angle - current_angle  # Ошибка управления
    control = P_control(Kp, error)  # Вычисляем управляющее воздействие
    motor.on(SpeedPercent(control))  # Подаем управляющее воздействие на двигатель

    # Если достигли целевого угла, останавливаем двигатель и выходим из цикла
    if abs(error) < 1:
        motor.stop()
        break

    time.sleep(0.2)  # Задержка для стабилизации системы