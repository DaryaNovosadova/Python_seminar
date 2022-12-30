# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности в том же порядке.

from random import randint

list_nums = []

numbers = int(input('Введите длину списка:'))
for i in range(numbers):
    list_nums.append(randint(1, 10))
print (list_nums)

if __name__ == '__main__':
    visited = set()
    dup = [x for x in list_nums if x in visited or (visited.add(x) or False)]
 
res = [x for x in dup + list_nums if x not in dup or x not in list_nums] 
print(res) 
