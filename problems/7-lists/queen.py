"""
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске,
определите, есть ли среди них пара бьющих друг друга.

Программа получает на вход восемь пар чисел,
каждое число от 1 до 8 — координаты 8 ферзей.
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""
queens_quantity = 8
under_attack_list = []

for coord_input in range(queens_quantity):
    queen_x, queen_y = [int(coordinate) for coordinate in input().split(sep=' ')]

    if [queen_x, queen_y] in under_attack_list:
        print('YES')
        break

    # print(queen_x, queen_y)
    # horizontal line
    for y in range(1, 9):
        if y != queen_y:
            under_attack_list.append([queen_x, y])
    # vertical line
    for x in range(1, 9):
        if x != queen_x:
            under_attack_list.append([x, queen_y])
    # main diagonal
    x, y = queen_x, queen_y
    while x < 8 and y > 1:
        x += 1
        y -= 1
        under_attack_list.append([x, y])
    x, y = queen_x, queen_y
    while x > 1 and y < 8:
        x -= 1
        y += 1
        under_attack_list.append([x, y])

    # secondary diagonal
    x, y = queen_x, queen_y
    while x < 8 and y < 8:
        x += 1
        y += 1
        under_attack_list.append([x, y])
    x, y = queen_x, queen_y
    while x > 1 and y > 1:
        x -= 1
        y -= 1
        under_attack_list.append([x, y])

    if coord_input == 7:
        print('NO')


# print(under_attack_list)
# print(len(under_attack_list))