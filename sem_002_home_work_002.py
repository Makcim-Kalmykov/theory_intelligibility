"""
Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
    1. Какова вероятность, что ни одна из них не перегорит в первый день? 
    2. Какова вероятность, что перегорят ровно две?
"""

from my_function import binomial_distribution, puasson_distributio

print("Задание 1:")
average = 0.0004 * 5000
e = 2.71828
print(f"p(X=0) = {round(puasson_distributio(average, 0, e) * 100, 6)} %")

# сравнение с формулой Бернули
print(f"p(X=0) = {round(binomial_distribution(0, 5000, 0.0004)*100, 6)} %")


print("Задание 2:")
average = 0.0004 * 5000
e = 2.71828
print(f"p(X=0) = {round(puasson_distributio(average, 2, e) * 100, 6)} %")

# сравнение с формулой Бернули
print(f"p(X=0) = {round(binomial_distribution(2, 5000, 0.0004)*100, 6)} %")
