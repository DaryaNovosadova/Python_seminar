#4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер плоскости:'))

if number == 1:
    print('Координаты X = от 0 до +бесконечности')
    print('Координаты Y = от 0 до +бесконечности')
elif number == 2:
    print('Координаты X = от 0 до -бесконечности')
    print('Координаты Y = от 0 до +бесконечности')
elif number == 3:
    print('Координаты X = от 0 до -бесконечности')
    print('Координаты Y = от 0 до -бесконечности')
elif number == 4:
    print('Координаты X = от 0 до +бесконечности')
    print('Координаты Y = от 0 до -бесконечности')
else:
    print('Число введено не корректно')