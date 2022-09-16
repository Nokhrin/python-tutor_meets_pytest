
# 1
"""
Дан список чисел.
Определите, сколько в нем встречается различных чисел.
Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""
# unique_count = len(set(int(number_str) for number_str in input().split(sep=' ')))
# print(unique_count)


# 2
"""
Даны два списка чисел. 
Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""
# set_a = set(input().split(sep=' '))
# set_b = set(input().split(sep=' '))
# elements_in_both_sets = set_a.intersection(set_b)
# print(len(elements_in_both_sets), end='')


# 3
"""
Даны два списка чисел. 
Найдите все числа, которые входят как в первый, так и во второй список 
и выведите их в порядке возрастания.
Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
"""
# set_a = set(int(number_str) for number_str in input().split(sep=' '))
# set_b = set(int(number_str) for number_str in input().split(sep=' '))
# elements_in_both_sets_sorted = sorted(list(set_a.intersection(set_b)))
# result_str = ' '.join([str(number) for number in elements_in_both_sets_sorted])
#
# print(result_str, end='')


"""
82 54 91 100 70 33 88 14 52 48 56 20 63 16 22 23 30 8 84 75 45 95 51 98 4 86 78 24 5 77 76 18 97 10 17 66 2 43 61 53 21 69 19 39 7 11 72 40 79 57 68 96 80 71 67 13 99 83 35 27 28 73 36 6 25 55
10 44 77 90 43 75 25 24 5 21 71 70 83 68 18 92 81 57 27 67 48 6 87 36 64 49 19 72 62 29 22 82 7 17 1 73 54 30 9 66 61 95 55 28 86 39 3 42 74 60 93 2 52 78 34 51 32 94 11 37 26 23 69 58 35 14 84
"""

# 4
"""
Во входной строке записана последовательность чисел через пробел. 
Для каждого числа выведите слово YES (в отдельной строке), 
если это число ранее встречалось в последовательности или NO, если не встречалось.
"""
numbers_list = [int(number) for number in input().split(sep=' ')]
numbers_set = set(numbers_list)
