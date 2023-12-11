import matplotlib.pyplot as plt

# Чтение данных из файла
data = []
with open('p075.txt', 'r') as file:
    for line in file:
        data.append(list(map(float, line.split())))

# Разделение данных на отдельные списки
time = [row[0] for row in data]
angle = [row[1] for row in data]
speed = [row[2] for row in data]

# Построение графика угла от времени
plt.figure(figsize=(10, 5))
plt.plot(time, angle)
plt.title('Угол от времени')
plt.xlabel('Время')
plt.ylabel('Угол')
plt.grid(True)
plt.show()

# Построение графика скорости от времени
plt.figure(figsize=(10, 5))
plt.plot(time, speed)
plt.title('Скорость от времени')
plt.xlabel('Время')
plt.ylabel('Скорость')
plt.grid(True)
plt.show()
