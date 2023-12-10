% Передаточная функция 1
s = tf('s');
T = 0.1;
k = 1;
w_1 = (k)/(T*s^2+s);
w_1.InputDelay = 0.2;
figure;


nyquist(w_1);
title('Годограф Найквиста');
hold on; 
plot(-1, 0, 'r*');
xline(0);
yline(0);
hold off; 
legend('Линия годографа', '(-1, 0)')
