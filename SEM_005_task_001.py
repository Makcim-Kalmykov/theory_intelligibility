"""
ЗАДАЧА 1
"""
import numpy as np
import scipy.stats as stats


x = np.array([2.5, 2.2, 2.6, 2.0, 2.1, 1.8, 2.4, 2.3, 2.7, 2.7, 1.9])
y = np.array([2.5, 1.7, 1.5, 2.5, 1.4, 1.9, 2.3, 2.0, 2.6, 2.3, 2.2])

x_mean = np.mean(x)                     # среднее арифметическое
y_mean = np.mean(y)
x_v = np.var(x, ddof=1)                 # дисперси несмещенная
y_v = np.var(y, ddof=1)
n_x = len(x)                            # кол-во наблюдений
n_y = len(y)
print(x_mean, y_mean, x_v, y_v, n_x, n_y)

t_emp = (x_mean - y_mean) / np.sqrt(x_v/n_x + y_v / n_y)
print(t_emp)

alpha = 0.05
n = n_x
t1 = stats.t.ppf(alpha / 2, df=2 * (n-1) )                    # квантильная ф-ия уровняя альфа. df - число степеней свободы n-1. 
t2 = stats.t.ppf(1 - alpha / 2, df=2 * (n-1) )                  # для двух выборок 2*n-1
print(t1, t2)                                           # критическое значение

print(stats.ttest_ind(x, y))                            # тест для сравнения средних двухвыборочный для независимых выборок

print(stats.ttest_1samp())