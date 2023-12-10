clear;

syms s;
syms t w positive;

ps = tf('s');

time_max = 30;
frequency_max = 5;

frequency_log_max = 3;

x0=100;
y0=100;
width=500;
height=500;

num_1 = [0 1 -3]; % числитель передаточной функции
den_1 = [1 7 4]; % знаменатель передаточной функции
num_2 = [100 40 4]; % числитель передаточной функции
den_2 = [100 -15 -8 -0.6]; % знаменатель передаточной функции
sys_1 = tf(num_1, den_1);
sys_2 = tf(num_2, den_2);
sys_1_d = (sys_1)/(1+sys_1);
sys_2_d = (sys_2)/(1+sys_2);

W = sys_1;

[Num,Den] = tfdata(W);
W_syms = poly2sym(cell2mat(Num),s)/poly2sym(cell2mat(Den),s);

disp('1. Передаточная функция:')
disp(W_syms);
disp('');

Step_response = ilaplace(W_syms * 1/s);
disp('2. Переходная характеристика:')
disp(Step_response);
disp('');

fplot(Step_response, [0, time_max], 'r', 'LineWidth', 2)
set(gcf,'units','points','position',[x0,y0,width,height]);
grid on
title('Переходная характеристика')
xlabel('t, с');
ylabel('Амплитуда');
saveas(gcf,'Step_response.png')
close all

Impulse_response = ilaplace(W_syms * 1);

disp('3. Весовая характеристика:')
disp(Impulse_response);
disp('');

fplot(Impulse_response, [0, time_max], 'r', 'LineWidth', 2)
set(gcf,'units','points','position',[x0,y0,width,height]);
grid on
title('Весовая характеристика')
xlabel('t, с');
ylabel('Амплитуда');
saveas(gcf,'Impulse_response.png')
close all

W_frequency = subs(W_syms, s, 1i*w);

disp('4. АЧХ и ФЧХ')
disp('W_frequency = ' + string(W_frequency));
disp('amplitude = ' + string(simplify(abs(W_frequency))));
disp('phase = ' + string(simplify(angle(W_frequency))));
disp('');

tiledlayout(2,1);
set(gcf,'units','points','position',[x0,y0,width,height]);
nexttile;
fplot(abs(W_frequency), [0, frequency_max], 'r', 'LineWidth', 2);
grid on
title('АЧХ');
xlabel('Частота (рад/сек)');
ylabel('Амплитуда');
nexttile;
fplot(angle(W_frequency)*180/pi, [0, frequency_max], 'r', 'LineWidth', 2);
grid on
title('ФЧХ');
xlabel('Частота (рад/сек)');
ylabel('Фаза (градусы)');
saveas(gcf,'АЧХ_и_ФЧХ.png')

