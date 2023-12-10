% Задаем передаточную функцию (пример: H(s) = (s + 1) / (s^2 + 2s + 2))
s = tf('s');
% G1 = 1/((s+1)*(s+2)*(s-3)*(s-4)*(s-5));
sys_1 = ((s-3.49)*(s+0.79))/((s-0.33)*(s-0.46)*(s+2.36)*(s+2)*(s-0.15));
sys_1_d = sys_1/(1+sys_1);
sys_2 = (s-3.94)/((s+1.04)*(s+0.34)*(s+1.9)*(s+1.38)*(s+0.67));
sys_2_d = sys_2/(1+sys_2);
sys_3 = ((s+3.09)*(s+1.47)*(s+2.17)*(s+0.86)*(s+1.13))/((s-1.01)*(s-0.67)*(s+0.34)*(s+3.97)*(s-0.24));
sys_3_d = sys_3/(1+sys_3);

k = 4;
w_1 = k * (s-3)/(s^2+7*s+4);
w_2 = k * (100*s^2+40*s+4)/(100*s^3-15*s^2-8*s-0.6);

% Вычисляем корни характеристического уравнения
poles = pole(w_1);

% Разделяем комплексные корни на действительные и мнимые части
real_poles = real(poles);
imag_poles = imag(poles);

% Строим график корней
figure;
scatter(real_poles, imag_poles, 'rx');
hold on;
%plot(real_poles, imag_poles, 'k--');% Добавляем линию ординат в точке x = 0
xline(0)

% Добавляем линию абцисс в точке y = 0
yline(0)
xlabel('Действительная часть');
ylabel('Мнимая часть');
title('График полюсов передаточной функции');
grid on;
legend('Корни');
