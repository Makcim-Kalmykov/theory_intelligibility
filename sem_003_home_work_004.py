"""
В университет на факультеты A и B поступило равное количество студентов, 
а на факультет C студентов поступило столько же, сколько на A и B вместе. 
Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
Студент сдал первую сессию. Какова вероятность, что он учится: 
    a). на факультете A 
    б). на факультете B 
    в). на факультете C?
"""

# a):
p1 = (0.8 * 0.25) / ((0.8 * 0.25) + (0.7 * 0.25) + (0.9 * 0.5))
print(round(p1, 5))

# б
p2 = (0.7 * 0.25) / ((0.8 * 0.25) + (0.7 * 0.25) + (0.9 * 0.5))
print(round(p2, 5))

# в):
p3 = (0.9 * 0.5) / ((0.8 * 0.25) + (0.7 * 0.25) + (0.9 * 0.5))
print(round(p3, 5))