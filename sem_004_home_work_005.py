"""
На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, 
от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?
"""
z = (190 - 178) / 25**(0.5)
print(z)