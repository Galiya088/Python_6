# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

'''first = int(input("Введите первый элемент: "))
raz = int(input("Введите разность: "))
count = int(input("Введите количество элементов: "))

list = []

for i in range(count):
    list.append(first + i*raz)

print(list)

'''
# Задача 32: Определить индексы элементов массива (списка),
#  значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


min_num = int(input("Введите заданный минимум: "))
max_num = int(input("Введите заданный максимум: "))
if min_num > max_num:
    min_num, max_num = max_num, min_num

count = int(input("Введите количество элементов: "))

list = []
list_diap = []

for i in range(count):
    num = int(input(f"Введите {i+1} элемент: "))
    list.append(num)
    if num >= min_num and num <= max_num:
        list_diap.append(num)

print(list)
print(f'{min_num, max_num} ->{list_diap}')
