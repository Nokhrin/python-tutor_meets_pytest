"""
Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов
этой последовательности равны друг другу.

Разрешено использовать простые переменные и цикл while
"""

curr_count = 0
max_count = 0
curr_number = int(input())
prev_number = None

while curr_number != 0:
    if curr_number == prev_number or prev_number is None:
        curr_count += 1
    else:
        curr_count = 1
    if curr_count > max_count:
        max_count = curr_count
    prev_number = curr_number
    curr_number = int(input())

print(max_count, end='')
