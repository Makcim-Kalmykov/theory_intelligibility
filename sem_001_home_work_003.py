"""
В ящике имеется 15 деталей, из которых 9 окрашены. 
Рабочий случайным образом извлекает 3 детали. 
Какова вероятность того, что все извлеченные детали окрашены?
"""
from math import factorial

def comb (num1, num2):
    return factorial(num2)/(factorial(num1)*factorial(num2-num1))

m = comb(3, 9)
n = comb(3, 15)
p = m / n

print(f"Вероятность события = {round(p, 4)} или {round(p *100, 2)}%")


# или 

p2 = (9/15)*(8/14)*(7/13)
print(round(p2 * 100, 2))