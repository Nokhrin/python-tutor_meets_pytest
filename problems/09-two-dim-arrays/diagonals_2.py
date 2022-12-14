"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.

Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""
size = int(input())
table = []
for i in range(size):
    row = []
    for j in range(size):
        if (i + j) < size - 1:
            row.append('0')
        elif (i + j) > size - 1:
            row.append('2')
        else:
            row.append('1')
    table.append(row)

for row in table:
    print(' '.join(row))
