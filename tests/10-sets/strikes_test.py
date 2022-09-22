import pytest

data_to_try = (
    ('19', ['2 3', '3 5', '9 8'], '8'),
    # ('5', ['1 2', '2 2'], '5')
)

task_ids = ['{}, {}, {}'.format(test_input[0], test_input[1], test_input[2]) for test_input in data_to_try]


@pytest.mark.parametrize('total_days, test_input, expected_output', data_to_try, ids=task_ids)
@pytest.mark.smoke
def test_strike(total_days, test_input, expected_output):
    days_in_year = int(total_days)
    strikes_count = len(test_input)
    strike_days = set()
    for i in range(strikes_count):
        start_day, interval = [int(number) for number in test_input[i].split(sep=' ')]
        day = start_day
        while day <= days_in_year:
            if (day + 1) % 7 != 0 and day % 7 != 0:  # if it's not saturday or sunday
                strike_days.add(day)
            day += interval

    assert str(len(strike_days)) == expected_output


@pytest.mark.parametrize(
    argnames='total_days, test_input, expected_output',
    argvalues=[
        ('19', ['2 3', '3 5', '9 8'], '8'),
        data_to_try
    ]
)
@pytest.mark.xfail(reason='check xfail functionality')
def test_strike_1(total_days, test_input, expected_output):
    days_in_year = int(total_days)
    strikes_count = len(test_input)
    strike_days = set()
    for i in range(strikes_count):
        start_day, interval = [int(number) for number in test_input[i].split(sep=' ')]
        day = start_day
        while day <= days_in_year:
            if (day + 1) % 7 != 0 and day % 7 != 0:  # if it's not saturday or sunday
                strike_days.add(day)
            day += interval

    assert len(strike_days) == expected_output


"""



1000 1
1 1



715

1000 1
179 1000



1

1000 1
700 1000



0

100000 2
746 23
9578 12



8231

100 3
39 68
62 17
7 72



3

1000 10
14 81
79 16
27 44
96 91
6 98
27 48
89 29
30 42
86 90
14 19



163
"""
