"""
В результате 10 независимых измерений некоторой величины X, выполненных с
одинаковой точностью,получены опытные данные:
6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
Предполагая, что результаты измерений подчинены нормальному закону распределения
вероятностей,оценить истинное значение величины X при помощи доверительного интервала,
покрывающего это значение с доверительной вероятностью 0,95.


p = x +- tα/2 * δ/√n
6.59 +- 2.2622 * 0,4508/√10

p(6.27 < μ < 6.91) = 0.95

"""

import numpy as np
a = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
x = np.mean(a)
print(x)
δ = np.std(a, ddof=1)
print(δ)
print(x - 2.2622 * δ/np.sqrt(len(a)))
print(x + 2.2622 * δ/np.sqrt(len(a)))