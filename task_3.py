# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
# эта точка (или на какой оси она находится).

# - x=34; y=-30 -> 4 # - x=2; y=4-> 1 # - x=-34; y=-30 -> 3

x = int(input('Введите координату х:'))
y = int(input('Введите координату у:'))

if x > 0 and y >0:
    print ('Точка координат находится в I координатной четверти')
elif x < 0 and y > 0:
    print ('Точка координат находится в II координатной четверти')
elif x < 0 and y < 0:
    print ('Точка координат находится в III координатной четверти')
elif x > 0 and y < 0:
    print ('Точка координат находится в IV координатной четверти')
else:
    print ('Введена нулевая координата по x или по y')
