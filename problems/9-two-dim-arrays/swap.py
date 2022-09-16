"""
Дан двумерный массив и два числа: i и j.
Поменяйте в массиве столбцы с номерами i и j и выведите результат.

Программа получает на вход размеры массива n и m,
затем элементы массива, затем числа i и j.

Решение оформите в виде функции swap_columns(a, i, j).
"""


def swap_columns(two_dim_array, first_column_number, second_column_number):
    """
    receive two-dimensional array and two numbers of columns, then swap that columns
    :param two_dim_array:
    :param first_column_number:
    :param second_column_number:
    :return: two-dimensional array with swapped columns
    """
    for i in range(len(two_dim_array)):
        two_dim_array[i][first_column_number], two_dim_array[i][second_column_number] = \
            two_dim_array[i][second_column_number], two_dim_array[i][first_column_number]

    return two_dim_array


rows_count, columns_count = [int(number) for number in input().split(sep=' ')]
table = [[number for number in input().split(sep=' ')] for row_index in range(rows_count)]
first_column, second_column = [int(number) for number in input().split(sep=' ')]
swapped_table = swap_columns(table, first_column, second_column)

print('\n'.join([' '.join([number for number in row]) for row in swapped_table]))
