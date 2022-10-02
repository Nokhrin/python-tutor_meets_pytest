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


def get_lca(pairs_count: str, node_1_and_node_2: list, requests_count: str, requests: list) -> list:
    """
    Find the lowest common ancestor (lca) of node_1 and node_2

    :param pairs_count: expected total number of child-parent paires to be processed
    :param node_1_and_node_2: list of strings with '<child name> <parent name>'
    :param requests_count: expected total number of requests
    :param requests: list of strings with requests
    :return: list of string, where each string is the name of lca
    """

    def find_lca(node_1, node_2, tree):
        """Return the lowest common ancestor of node_1 and node_2 from tree."""
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

    entries_count = int(pairs_count)
    child_parent_pairs_dict = dict()
    for i in range(entries_count - 1):
        child, parent = node_1_and_node_2[i].split(sep=' ')
        child_parent_pairs_dict[child] = parent

    requests_count = int(requests_count)
    lca_list = []
    for r in range(requests_count):
        name_1, name_2 = requests[r].split(sep=' ')
        # print(find_lca(name_1, name_2, child_parent_pairs_dict), end='')
        lca_list.append(find_lca(name_1, name_2, child_parent_pairs_dict))
        # if r < requests_count - 1:
        #     print()
    return lca_list
