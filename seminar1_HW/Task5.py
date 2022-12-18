#5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. 

X1 = float(input('Введите X1:'))
Y1 = float(input('Введите Y1:'))
X2 = float(input('Введите X2:'))
Y2 = float(input('Введите Y2:'))

import math
distance = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
print(distance)