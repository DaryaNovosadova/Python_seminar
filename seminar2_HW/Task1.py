# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Без работы с методами строк.


num = float(input('Введите число:'))
while(num != int(num)):
    num *= 10
num = int(num)
print(num)
sum = 0
while(num > 0): 
    sum = sum + num % 10
    num //= 10
print(int(sum))
