# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def spisok(count, word = 'абв'):
    my_list = []
    for i in range(count):
        temp = sample(word, k = 3)
        my_list.append(''.join(temp))
    return my_list

a = spisok(int(input()))

def find_num(my_list):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] != 'абв':
            new_list.append(my_list[i])
    return new_list
print(a)
print(find_num(a))
