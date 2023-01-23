# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

N = int(input('Введите число N:'))
lst = [i for i in range(20, N + 1)]

def creat_list(lst):
    new_list = []
    for i in range(len(lst)):
        if lst[i] % 20 == 0:
            new_list.append(lst[i])
        if lst[i] % 21 == 0:
            new_list.append(lst[i])
    return new_list

print(creat_list(lst))
