import pytest
from problems.sets import strike

data_to_try = [
    ('19 3', ['2 3', '3 5', '9 8'], '8'),
    ('5 2', ['1 2', '2 2'], '5'),
    pytest.param('5', ['1 2', '2 2'], '6', marks=pytest.mark.xfail),
    ('1000 1', ['1 1'], '715'),
    ('1000 1', ['179 1000'], '1'),
    ('1000 1', ['700 1000'], '0'),
    ('100000 2', ['746 23', '9578 12'], '8231'),
    ('100 3', ['39 68', '62 17', '7 72'], '3'),
    ('1000 10', ['14 81', '79 16', '27 44', '96 91', '6 98', '27 48', '89 29', '30 42', '86 90', '14 19'], '163'),
]

input_ids = ['{}, {}, {}'.format(test_input[0], test_input[1], test_input[2]) for test_input in data_to_try]


@pytest.mark.parametrize(
    'total_days_and_schedules, schedules, expected',
    data_to_try,
    ids=input_ids
)
class TestStrikes:
    @pytest.mark.smoke
    def test_strike(self, total_days_and_schedules, schedules, expected):
        """checks for correct output of count_strikes"""
        actual = strike.count_strikes(total_days_and_schedules, schedules)
        assert actual == expected

    def test_input_data(self, total_days_and_schedules: str, schedules: list, expected: str):
        expected_schedules_count = int(total_days_and_schedules.split(sep=' ')[1])
        actual_schedules_count = len(schedules)
        assert actual_schedules_count == expected_schedules_count, 'required and actual schedules count doesn\'t match'
