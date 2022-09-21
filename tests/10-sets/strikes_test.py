import pytest


@pytest.mark.parametrize(
    argnames='total_days, test_input, expected_output',
    argvalues=[
        ('19', ['2 3', '3 5', '9 8'], '8')
    ]
)
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


"""

5 2
1 2
2 2



5

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
