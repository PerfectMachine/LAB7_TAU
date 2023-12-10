import json
import matplotlib.pyplot as plt


def json_to_dict(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    data = json_to_dict('data.json')
    angles = [d['angle'] for d in data]
    times = [d['time'] for d in data]

    # Создаем график
    plt.plot(times, angles)
    plt.grid()
    # Добавляем названия осей
    plt.xlabel('Время')
    plt.ylabel('Угол')

    # Показываем график
    plt.show()