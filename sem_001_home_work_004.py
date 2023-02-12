"""
В лотерее 100 билетов. Из них 2 выигрышных. 
Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
"""

from math import factorial

def comb (num1, num2):
    return factorial(num2)/(factorial(num1)*factorial(num2-num1))

p = (2/100)*(1/99)
print(f"P(A) = {round(p * 100, 2)}%")


# вариант б:

m = comb(2, 2) # равно 1
n = comb(2, 100)
p2 = m / n
print(f"P(A) = {round(p2 * 100, 2)}%")