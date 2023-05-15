# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент(a1), 
# разность(d) и количество элементов(n) нужно ввести с клавиатуры. Формула для получения n-го 
# члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Input:
# 1 - a1
# 2 - d
# 5 - n
# Output:
# 1, 3, 5, 7, 9

first_element = int(input('first element: '))
dif = int(input('difference: '))
len = int(input('Len array: '))
array = [first_element + i * dif for i in range(len)]
print(array)