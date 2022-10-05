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


def get_input(max_num, guess_response):
    """Retrieve maximum guessed number and sets of guesses from user."""
    max_number = int(max_num)
    guess_sets_list = []
    input_count = 0
    while True:
        user_input = guess_response[input_count]
        if user_input != 'HELP':
            guess_numbers_set = set([int(number) for number in user_input.split(sep=' ')])
            guess_sets_list.append(guess_numbers_set)
        else:
            return max_number, guess_sets_list
        input_count += 1


def get_possible_numbers(max_num_input: str, guess_input: list) -> list:
    numbers_count, list_of_guesses = get_input(max_num_input, guess_input)
    whole_numbers_set = set(i for i in range(1, numbers_count + 1))
    possible_numbers_set = whole_numbers_set

    responses_list = []
    for guess_set in list_of_guesses:
        current_set = possible_numbers_set & guess_set
        if len(current_set) <= len(possible_numbers_set) // 2:
            responses_list.append('NO')
            possible_numbers_set = possible_numbers_set - guess_set
        else:
            responses_list.append('YES')
            possible_numbers_set = possible_numbers_set - (whole_numbers_set - guess_set)

    possible_numbers_list = [str(number) for number in sorted(list(possible_numbers_set))]
    responses_list.append(' '.join(possible_numbers_list))
    return responses_list
