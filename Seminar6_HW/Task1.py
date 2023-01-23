# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import choices

n = int(input('Введите размер списка: '))
my_list = [i for i in choices(range(30), k = n)]

def SortList(my_list):
    new_list = []
    for i in range(len(my_list) - 1):
        if my_list[i] < my_list[i+1]:
            new_list.append(my_list[i+1])
    return new_list


print(my_list)
print(SortList(my_list))


