# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

list_nums = []

num = int(input('Введите длину списка:'))
for i in range(num):
    list_nums.append(randint(1, 10))
print (list_nums)

def new_list(list_nums):
    new_list = []
    len_list = len(list_nums)
    for i in range(len_list // 2):
        new_list.append(list_nums[i] * list_nums[len_list - i - 1])
    if len_list % 2:
        new_list.append(list_nums[len_list // 2])
    return new_list
print(new_list(list_nums))