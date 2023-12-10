% Определение передаточной функции открытой системы

num_1 = [0 1 -3]; % числитель передаточной функции
den_1 = [1 7 4]; % знаменатель передаточной функции
num_2 = [100 40 4]; % числитель передаточной функции
den_2 = [100 -15 -8 -0.6]; % знаменатель передаточной функции
sys_1 = tf(num_1, den_1);
sys_2 = tf(num_2, den_2);

sys = sys_2;
% Описание диапазона изменения коэффициента запаздывания `tau`
tau = linspace(0, 1, 1000); % от 0 до 1 с 1000 значениями в этом диапазоне

% Вычисление корневого локуса для каждого `tau`
rlocus_points = arrayfun(@(t) pole(feedback(series(sys, tf([1], [t 1])))), tau, 'UniformOutput', false);

% Определение количества неустойчивых полюсов для кажого `tau`
% Неустойчивые полюса имеют положительную вещественную часть
num_unstable_poles = cellfun(@(poles) sum(real(poles) > 0), rlocus_points);

% Отображение графика
figure;
plot(tau, num_unstable_poles, 'b-', 'LineWidth', 2);
xlabel('Коэффициент запаздывания tau');
ylabel('Количество неустойчивых полюсов');
title('Зависимость количества неустойчивых полюсов от коэффициента запаздывания');
grid on;
