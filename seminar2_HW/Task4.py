# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

N = int(input('Введите число N:'))
lst = [round(i, 3) for i in range(-N, N + 1)]
print(lst)
a = int(input('Введите число первой позиции:'))
b = int(input('Введите число второй позиции:'))
result = lst[a - 1] * lst[b - 1]
print(result)