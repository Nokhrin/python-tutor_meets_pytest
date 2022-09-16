"""
Август и Беатриса продолжают играть в игру, но Август начал жульничать.
На каждый из вопросов Беатрисы он выбирает такой вариант ответа YES или NO,
чтобы множество возможных задуманных чисел оставалось как можно больше.
Например, если Август задумал число от 1 до 5, а Беатриса спросила про числа 1 и 2,
то Август ответит NO, а если Беатриса спросит про 1, 2, 3, то Август ответит YES.

Если же Бетриса в своем вопросе перечисляет ровно половину из задуманных чисел,
то Август из вредности всегда отвечает NO.
Наконец, Август при ответе учитывает все предыдущие вопросы Беатрисы и свои ответы на них,
то есть множество возможных задуманных чисел уменьшается.

Первая строка содержит наибольшее число, которое мог загадать Август.
Каждая следующая строка содержит очередной вопрос Беатрисы: набор чисел, разделенных пробелами.
Последняя строка входных данных содержит одно слово HELP.

Для каждого вопроса Беатрисы выведите ответ Августа на этот вопрос.
После этого выведите через пробел, в порядке возрастания, все числа,
которые мог загадать Август после ответа на все вопросы Беатрисы.
"""


def get_input():
    """retrieve maximum guessed number and sets of guesses from user"""
    max_number = int(input())
    guess_sets_list = []
    while True:
        user_input = input()
        if user_input != 'HELP':
            guess_numbers_set = set([int(number) for number in user_input.split(sep=' ')])
            guess_sets_list.append(guess_numbers_set)
        else:
            return max_number, guess_sets_list


numbers_count, list_of_guesses = get_input()
wrong_numbers_set = set()
possibly_right_numbers_set = set(i for i in range(1, numbers_count + 1))

for guess_set in list_of_guesses:
    if len(guess_set) <= numbers_count // 2:
        possibly_right_numbers_set.difference_update(guess_set)
        print(len(guess_set))
        print(len(possibly_right_numbers_set))
        print('NO')
    else:
        possibly_right_numbers_set.intersection_update(guess_set)
        print('YES')

possible_numbers_list = [str(number) for number in sorted(list(possibly_right_numbers_set))]
result_str = ' '.join(possible_numbers_list)
print(result_str)
