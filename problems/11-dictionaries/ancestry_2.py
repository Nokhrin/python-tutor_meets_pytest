"""
Даны два элемента в дереве.
Определите, является ли один из них потомком другого.

Программа получает на вход число элементов в генеалогическом древе N.
Далее следует N−1 строка, задающие родителя для каждого элемента древа, кроме родоначальника.
Каждая строка имеет вид имя_потомка имя_родителя.

Далее идет число запросов K. В каждой из следующих K строк, содержатся имена двух элементов дерева.

Для каждого такого запроса выведите одно из трех чисел:
1, если первый элемент является предком второго,
2, если второй является предком первого
или 0, если ни один из них не является предком другого.
"""

entries_count = int(input())
pairs_input = dict()
unique_elements = list()

for i in range(entries_count - 1):
    child, parent = input().split(sep=' ')
    pairs_input[child] = parent
    if child not in unique_elements:
        unique_elements.append(child)
    if parent not in unique_elements:
        unique_elements.append(parent)


# adjacency list
parent_children_dict = dict()
for name in unique_elements:
    parent_children_dict[name] = []
    for child, parent in pairs_input.items():
        if parent == name:
            parent_children_dict[name].append(child)

# print(parent_children_dict)


def is_child_of_parent(child_check, parent_check, tree):
    """returns True if parent_check is ancestor of child_check, else returns False"""
    list_to_visit = [parent_check]
    visited_list = []
    while list_to_visit:
        next_to_visit = list_to_visit.pop(0)
        if next_to_visit not in visited_list:
            visited_list.append(next_to_visit)
            if next_to_visit in tree.keys():
                for next_child in tree[next_to_visit]:
                    list_to_visit.append(next_child)
            else:
                print('no children here')
        else:
            print('already visited')

    # print(visited_list)  # who has been visited up from parent_check
    return child_check in visited_list


requests_count = int(input())
answer_list = []
for i in range(requests_count):
    node_1, node_2 = input().split(sep=' ')

    if is_child_of_parent(node_1, node_2, parent_children_dict):
        answer_list.append('2')
    elif is_child_of_parent(node_2, node_1, parent_children_dict):
        answer_list.append('1')
    else:
        answer_list.append('0')

print(' '.join(answer_list), end='')
