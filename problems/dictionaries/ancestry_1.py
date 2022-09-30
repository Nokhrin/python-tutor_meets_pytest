"""
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.

Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.

Вам дано генеалогическое древо, определите высоту всех его элементов.

Программа получает на вход число элементов в генеалогическом древе N.
Далее следует N−1 строка, задающие родителя для каждого элемента древа, кроме родоначальника.
Каждая строка имеет вид имя_потомка имя_родителя.

Программа должна вывести список всех элементов древа в лексикографическом порядке.
После вывода имени каждого элемента необходимо вывести его высоту.
"""

children_count = int(input())
child_parent_dict = dict()

parents_list = []

for i in range(children_count - 1):
    child, parent = input().split(sep=' ')
    if child not in child_parent_dict.keys():
        child_parent_dict[child] = parent
        parents_list.append(parent)

for parent in parents_list:
    if parent not in child_parent_dict.keys():
        child_parent_dict[parent] = ''

parents_h_dict = dict()
height = 0
# find root parent (with height = 0)
for child, parent in child_parent_dict.items():
    if parent == '':
        parents_h_dict[child] = height

# count height
iter_counter = len(child_parent_dict)
while iter_counter > 0:
    for child, parent in child_parent_dict.items():
        if parent in parents_h_dict.keys():
            parents_h_dict[child] = parents_h_dict[parent] + 1
    iter_counter -= 1

# print result
names_sorted_list = sorted([name for name in parents_h_dict.keys()])
for name in names_sorted_list:
    print(name, parents_h_dict[name])
