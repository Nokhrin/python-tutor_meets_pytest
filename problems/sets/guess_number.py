"""
Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае. После нескольких заданныъх вопросов Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.

В первой строке задано n - максимальное число, которое мог загадать Август.
Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных пробелом)
и ответ Августа на этот вопрос.

Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.
"""

def get_possible_numbers(max_num: str, guess_response: list) -> str:
    """
    Return possible secret numbers

    :param max_num: maximum secret number
    :param guess_numbers: string with guess
    :return: string with possible secret numbers
    """
    max_number = int(max_num)
    possible_numbers_set = set()

    input_count = 0
    while True:
        guess = guess_response[input_count]
        input_count += 1
        if guess == 'HELP':
            break
        else:
            guess_numbers_set = set([int(number) for number in guess.split(sep=' ')])
            response = guess_response[input_count]

        if response == 'YES':
            if len(possible_numbers_set) == 0:
                possible_numbers_set = guess_numbers_set
            else:
                possible_numbers_set.intersection_update(guess_numbers_set)
        elif response == 'NO':
            possible_numbers_set.difference_update(guess_numbers_set)
        input_count += 1

    sorted_numbers_list = sorted(list(possible_numbers_set))
    return ' '.join([str(number) for number in sorted_numbers_list])
