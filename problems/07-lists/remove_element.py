"""
Дан список из чисел и индекс элемента в списке k.
Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.

Программа получает на вход список, затем число k.
Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
Также нельзя использовать дополнительный список.
Также не следует использовать метод pop(k) с параметром.
"""

numbers_list = [int(number) for number in input().split(sep=' ')]
index_to_remove = int(input())

# with slicing
# numbers_list = numbers_list[:index_to_remove] + numbers_list[index_to_remove + 1:]
# numbers_list = [str(number) for number in list_after_remove]

# with pop()
for i in range(index_to_remove, len(numbers_list) - 1):
    numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[index_to_remove]

numbers_list.pop()
numbers_list = [str(number) for number in numbers_list]
result = ' '.join(numbers_list)

print(result)
