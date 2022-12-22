# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.


n = int(input('Введите число:'))
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(lst)
sum = round(sum(lst), 3)
print(sum)