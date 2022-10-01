"""
Политическая жизнь одной страны очень оживленная.
В стране действует K политических партий, каждая из которых регулярно объявляет национальную забастовку.
Дни, когда хотя бы одна из партий объявляет забастовку,
при условии, что это не суббота или воскресенье (когда и так никто не работает),
наносят большой ущерб экономике страны.

i-я партия объявляет забастовки строго каждые b_i дней,
начиная с дня с номером a_i.
То есть i-я партия объявляет забастовки в дни a_i, a_i + b_i, a_i + 2 * b_i и т.д.
Если в какой-то день несколько партий объявляет забастовку,
то это считается одной общенациональной забастовкой.

В календаре страны N дней, пронумерованных, начиная с единицы.
Первый день года является понедельником, шестой и седьмой дни года — выходные, неделя состоит из семи дней.

В первой строке даны числа N и K.
Далее идет K строк, описывающие графики проведения забастовок.
i-я строка содержит числа a_i и b_i.
Вам нужно определить число забастовок, произошедших в этой стране в течение года.
"""

def count_strikes(N_and_K: str, schedules: list) -> int:
    """
    :param N_and_K: N - days in the year count; K - following input strings count
    :param schedules: strikes schedule list of a_i (start day) and b_i (days between strikes)
    :return: number of days in strikes
    """
    days_in_year, strikes_count = [int(number) for number in N_and_K.split(sep=' ')]
    strike_days = set()
    for i in range(strikes_count):
        for schedule in schedules:
            schedule_list = schedule.split(sep=' ')
            start_day, interval = int(schedule_list[0]), int(schedule_list[1])
            day = start_day
            while day <= days_in_year:
                if (day + 1) % 7 != 0 and day % 7 != 0:  # if it's not saturday or sunday
                    strike_days.add(day)
                day += interval

    return str(len(strike_days))
