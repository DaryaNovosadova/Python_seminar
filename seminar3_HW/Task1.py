# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

list_nums = []
len_list = int(input('Введите длинну списка '))
list_nums = sample(range(1, len_list * 2), k = len_list)
print(list_nums)

def get_sum():
    sum = 0
    for i in range(0, len(list_nums), 2):
        sum += list_nums[i]
    return sum
print(get_sum())