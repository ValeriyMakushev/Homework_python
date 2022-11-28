'''Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой
 оси она находится).
Пример:
 - x=34; y=-30 -> 4
 - x=2; y=4-> 1
- x=-34; y=-30 -> 3'''

x = int(input('Введите число x не равное 0:'))
y = int(input('Введите число y не равное 0:'))
if x > 0 and y > 0:
    print('Точка находится в I четверти')
elif x < 0 and y > 0:
    print('Точка находится в II четверти')
elif x < 0 and y < 0:
    print('Точка находится в III четверти')
elif x > 0 and y < 0:
    print('Точка находится в IV четверти')
