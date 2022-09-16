"""
N кеглей выставили в один ряд,
занумеровав их слева направо числами от 1 до N.
Затем по этому ряду бросили K шаров,
при этом i-й шар сбил все кегли с номерами от li до ri включительно.

Определите, какие кегли остались стоять на месте.

Программа получает на вход количество кеглей N и количество бросков K.
Далее идет K пар чисел li, ri, при этом 1 ≤ li ≤ ri ≤ N.

Программа должна вывести последовательность из N символов,
где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""
pins, shots = [int(number) for number in input().split(sep=' ')]
pins_list = ['I'] * pins

for i in range(shots):  # read input for each shot
    left, right = [int(position) for position in input().split(sep=' ')]
    for j in range(left - 1, right):
        pins_list[j] = '.'

pins_str = ''.join(pins_list)
print(pins_str)
