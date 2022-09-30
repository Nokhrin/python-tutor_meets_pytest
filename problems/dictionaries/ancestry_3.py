"""
В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common Ancestor).

Наименьшим общим предком элементов A и B является такой элемент C,
что С является предком A, C является предком B, при этом глубина C является наибольшей из возможных.
При этом элемент считается своим собственным предком.

Программа получает на вход число элементов в генеалогическом древе N.
Далее следует N−1 строка, задающие родителя для каждого элемента древа, кроме родоначальника.
Каждая строка имеет вид имя_потомка имя_родителя.

Далее идет число запросов K. В каждой из следующих K строк, содержатся имена двух элементов дерева.

Для каждого запроса выведите наименьшего общего предка данных элементов.
"""


def find_lca(node_1, node_2, tree):
    """returns the lowest common ancestor of node_1 and node_2 from tree"""
    next_parent = node_1
    node_1_parents = [node_1]
    while next_parent in tree.keys():
        node_1_parents.append(tree[next_parent])
        next_parent = tree[next_parent]

    next_parent = node_2
    node_2_parents = [node_2]

    while next_parent in tree.keys():
        node_2_parents.append(tree[next_parent])
        next_parent = tree[next_parent]

    for parent_1 in node_1_parents:
        if parent_1 in node_2_parents:
            return parent_1


entries_count = int(input())
child_parent_pairs_dict = dict()
for i in range(entries_count - 1):
    child, parent = input().split(sep=' ')
    child_parent_pairs_dict[child] = parent

requests_count = int(input())
for r in range(requests_count):
    name_1, name_2 = input().split(sep=' ')
    print(find_lca(name_1, name_2, child_parent_pairs_dict), end='')
    if r < requests_count - 1:
        print()
