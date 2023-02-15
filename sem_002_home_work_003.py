"""
Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
"""

from my_function import binomial_distribution

p = binomial_distribution(70, 144, 0.5)
print(round(p*100, 4))