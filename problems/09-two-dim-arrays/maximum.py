"""
Найдите индексы первого вхождения максимального элемента.
Выведите два числа: номер строки и номер столбца,
в которых стоит наибольший элемент в двумерном массиве.

Если таких элементов несколько, то выводится тот, у которого меньше номер строки,
а если номера строк равны то тот, у которого меньше номер столбца.

Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
"""


def get_first_num_indexes(search_number, two_dim_array):
    """
    finds first appearance of provided number
    :return indexes of the number as strings
    """
    for row_index in range(len(two_dim_array)):
        for column_index in range(len(two_dim_array[i])):
            if two_dim_array[row_index][column_index] == search_number:
                return [str(row_index), str(column_index)]


rows_count, columns_count = [int(number) for number in input().split(sep=' ')]
table = []
max_num = None
for i in range(rows_count):
    row = [int(number) for number in input().split(sep=' ')]
    for number in row:
        if max_num is None or number > max_num:
            max_num = number
    table.append(row)

print(' '.join(get_first_num_indexes(max_num, table)))
