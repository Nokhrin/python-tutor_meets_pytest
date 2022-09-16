## 1
# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
# a_list = input().split(' ')
# evens_list = a_list[::2]
# print(' '.join(evens_list))

## 2
# Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
# list_input = [int(str_num) for str_num in input().split()]
# for element in list_input:
#     if element % 2 == 0:
#         print(element, end=' ')


## 3
# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# numbers_list = [int(str_num) for str_num in input().split(sep=' ')]
# for i in range(1, len(numbers_list)):
#     if numbers_list[i] > numbers_list[i - 1]:
#         print(numbers_list[i], end=' ')


## 4
# Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
# Если соседних элементов одного знака нет — не выводите ничего.
# Если таких пар соседей несколько — выведите первую пару.

# numbers_list = [int(str_num) for str_num in input().split(sep=' ')]
# first_two_same_sign = []
# for i in range(1, len(numbers_list)):
#     prev_element = numbers_list[i - 1]
#     curr_element = numbers_list[i]
#     if prev_element * curr_element > 0:
#         first_two_same_sign = [str(prev_element), str(curr_element)]
#         break
#
# str_output = ' '.join(first_two_same_sign)
# if len(first_two_same_sign):
#     print(str_output, end='')


## 5
# Дан список чисел.
# Определите, сколько в этом списке элементов, которые больше двух своих соседей,
# и выведите количество таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.

# numbers_list = [int(str_numbers) for str_numbers in input().split(sep=' ')]
# greatest_count = 0
# for number_index in range(1, len(numbers_list) - 1):
#     previous_number = numbers_list[number_index - 1]
#     current_number = numbers_list[number_index]
#     next_number = numbers_list[number_index + 1]
#     if current_number > previous_number and current_number > next_number:
#         greatest_count += 1
# greatest_count = str(greatest_count)
# print(greatest_count, end='')


## 6
# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.

# numbers_list = [int(number) for number in input().split(sep=' ')]
# max_number = max(numbers_list)
# max_number_index = numbers_list.index(max_number)
#
# print(max_number, max_number_index, sep=' ', end='')


## 7
# numbers_list = [int(number) for number in input().split(sep=' ')]
# count_unique = 1
# if len(numbers_list) > 1:
#     for i in range(1, len(numbers_list)):
#         count_unique += int(numbers_list[i] != numbers_list[i - 1])
#
# print(count_unique)


## 8
# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.
# numbers_list = [int(number) for number in input().split(sep=' ')]
# numbers_switched = []
# for i in range(0, len(numbers_list) - 1, 2):
#     numbers_switched = numbers_switched + [numbers_list[i + 1], numbers_list[i]]
#
# if len(numbers_list) % 2 != 0:
#     numbers_switched.append(numbers_list[-1])
#
# numbers_list_str = [str(number) for number in numbers_switched]
# print(' '.join(numbers_list_str))


## 9
# """В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка. """
# numbers_list = [int(number) for number in input().split(sep=' ')]
# min_element_index = numbers_list.index(min(numbers_list))
# max_element_index = numbers_list.index(max(numbers_list))
# numbers_list[min_element_index], numbers_list[max_element_index] = numbers_list[max_element_index], numbers_list[min_element_index]
#
# print(' '.join([str(number) for number in numbers_list]), end='')


## 10
"""
Дан список из чисел и индекс элемента в списке k.
Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.

Программа получает на вход список, затем число k.
Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
Также нельзя использовать дополнительный список.
Также не следует использовать метод pop(k) с параметром.
"""

# numbers_list = [int(number) for number in input().split(sep=' ')]
# index_to_remove = int(input())
#
# # with slicing
# # numbers_list = numbers_list[:index_to_remove] + numbers_list[index_to_remove + 1:]
# # numbers_list = [str(number) for number in list_after_remove]
#
# # with pop()
# for i in range(index_to_remove, len(numbers_list) - 1):
#     numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[index_to_remove]
#
# numbers_list.pop()
# numbers_list = [str(number) for number in numbers_list]
# result = ' '.join(numbers_list)
#
# print(result)



## 11
"""
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k 
элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Поскольку при этом количество элементов в списке увеличивается, 
после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.
Вставку необходимо осуществлять уже в считанном списке, 
не делая этого при выводе и не создавая дополнительного списка.
"""
# numbers_list = [int(number) for number in input().split(sep=' ')]
# index_to_insert, number_to_insert = [int(number) for number in input().split(sep=' ')]
#
# # extend the list
# numbers_list.append(0)
# for i in range(index_to_insert, len(numbers_list)):
#     curr_num = numbers_list[i]
#
#     if i == index_to_insert:
#         numbers_list[i] = number_to_insert
#     else:
#         numbers_list[i] = next_num
#
#     next_num = curr_num
#
# numbers_list_str = ' '.join([str(number) for number in numbers_list])
# print(numbers_list_str, end='')


## 12
