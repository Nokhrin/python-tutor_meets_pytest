"""
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю.
Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел,
означающих рост каждого человека в строю.
После этого вводится число X – рост Пети.
Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй.
Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
"""

rank_list = [int(height) for height in input().split(sep=' ')]
height_to_insert = int(input())
index_to_paste = len(rank_list)  # assume all numbers are higher, append to the end of the list in that case

for i in range(len(rank_list)):
    height = rank_list[i]
    if height < height_to_insert:
        index_to_paste = i
        break

new_rank_list = rank_list[:index_to_paste] + [height_to_insert] + rank_list[index_to_paste:]
new_rank_str = ' '.join([str(height) for height in new_rank_list])
# print(new_rank_str)
# shift by 1 because indexes in lists start with 0, but in ranks people are numbered starting with 1
number_in_rank = index_to_paste + 1
print(number_in_rank)
