# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def factors(num):
    list_new = []
    i = 2
    while i <= num:
        if num % i == 0:
            list_new.append(i)
            num //= i
        else:
            i += 1
    if num > 1:
            list_new.append(num)
    return list_new
print(factors(int(input('Введите число: '))))
