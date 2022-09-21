"""
Дано число n.
Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0.
На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
"""
size = int(input())
table = []
for i in range(size):
    row = []
    for j in range(size):
        cell_value = abs(j - i)
        row.append(str(cell_value))
    table.append(row)

for row in table:
    print(' '.join(row))
