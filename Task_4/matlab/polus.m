
num_1 = [0 1 -3]; 
den_1 = [1 7 4]; 
num_2 = [100 40 4]; 
den_2 = [100 -15 -8 -0.6]; 
sys_1 = tf(num_1, den_1);
sys_2 = tf(num_2, den_2);


sys = sys_2;

k = linspace(-1000, 1000, 100000);


[rlocus_points, k_values] = rlocus(sys, k);


num_unstable_poles = arrayfun(@(ki) sum(real(rlocus_points(:, ki)) > 0), 1:length(k));


figure;
plot(k, num_unstable_poles, 'b-', 'LineWidth', 2);
xlabel('Коэффициент усиления k');
ylabel('Количество неустойчивых полюсов');
title('Зависимость количества неустойчивых полюсов от коэффициента усиления');
grid on;
