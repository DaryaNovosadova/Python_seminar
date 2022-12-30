# 1. Вычислить число c заданной точностью d

from decimal import Decimal

num = float(input('Введите число: '))
c = str(input("Введите требуемую точность '0.001': "))
number = Decimal(num)
number = number.quantize(Decimal(c))
print(number)