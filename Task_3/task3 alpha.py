import ev3dev.ev3 as ev3
import matplotlib.pyplot as plt
import numpy as np

# Константы для настройки моторов и датчиков EV3
left_motor = ev3.LargeMotor('outA')
right_motor = ev3.LargeMotor('outD')
gyro_sensor = ev3.GyroSensor()
sonar_sensor = ev3.UltrasonicSensor()

# Функция для записи данных о показаниях гироскопа и ультразвукового датчика
def collect_data():
    gyro_data = []
    sonar_data = []
    for i in range(10):
        gyro_data.append(gyro_sensor.value())
        sonar_data.append(sonar_sensor.value())
    return gyro_data, sonar_data

# Функция для управления моторами в зависимости от заданной частоты
def set_motors_power(freq):
    power = int(freq * 100)
    left_motor.run_direct(duty_cycle_sp=power)
    right_motor.run_direct(duty_cycle_sp=power)

# Функция для рассчёта амплитудно-частотной характеристики (ЧАХ)
def plot_amplitude_frequency_response():
    frequencies = range(5, 105, 5)
    amplitudes = []
    for frequency in frequencies:
        set_motors_power(frequency)
        gyro_data, sonar_data = collect_data()
        # Вычисляем амплитуду по данным гироскопа и ультразвукового датчика
        amplitude = np.mean(gyro_data) + np.mean(sonar_data)
        amplitudes.append(amplitude)
    plt.plot(frequencies, amplitudes)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Amplitude-Frequency Response')
    plt.show()

# Функция для рассчёта фазово-частотной характеристики (ФЧХ)
def plot_phase_frequency_response():
    frequencies = range(5, 105, 5)