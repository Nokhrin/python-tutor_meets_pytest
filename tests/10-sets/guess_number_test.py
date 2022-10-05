import pytest
from problems.sets.guess_number import get_possible_numbers


@pytest.mark.parametrize(
    argnames='max_number, actual_input, expected_result',
    argvalues=[
        ('10',
        ['1 2 3 4 5', 'YES', '2 4 6 8 10', 'NO', 'HELP'],
        '1 3 5'),
        ('10',
        ['1 2 3 4 5 6 7 8 9 10', 'YES', '1', 'NO', '2', 'NO', '3', 'NO', '4', 'NO', '6', 'NO', '7', 'NO', '8', 'NO', '9', 'NO', '10', 'NO', 'HELP'],
        '5'),
        ('100',
        ['3 5 8 10 11 13 14 15 16 20 21 23 25 27 29 31 32 33 35 42 43 46 47 48 51 52 57 58 67 68 72 74 75 76 79 80 81 82 83 84 86 89 90 91 92 93 94 95 96 99', 'YES', '1 4 7 9 14 16 17 19 20 23 25 27 28 29 30 31 32 33 41 42 45 46 48 50 52 54 59 60 61 63 66 67 68 69 70 71 73 74 79 81 82 83 89 90 91 92 93 94 95 100', 'YES', '3 5 6 15 16 18 19 20 21 22 23 24 26 28 29 35 37 38 39 40 41 43 44 45 46 47 53 55 56 60 61 63 64 65 68 70 71 73 76 79 80 81 82 83 86 90 91 95 96 99', 'YES', '1 2 3 5 11 16 17 23 25 31 32 33 34 35 38 39 41 43 44 46 47 49 51 53 58 59 62 63 68 69 70 72 73 74 76 77 78 79 80 81 82 83 85 86 93 94 95 97 99 100', 'YES', '3 7 8 9 10 14 17 20 22 23 24 25 26 27 28 30 34 40 42 43 45 47 48 49 50 51 52 53 54 55 59 62 63 66 67 72 73 75 77 81 83 84 86 89 92 93 94 96 98 100', 'YES', 'HELP'],
         '23 81 83'),
    ]
)
def test_get_possible_number(max_number, actual_input, expected_result):
    """Test output of get_possible_numbers."""
    assert expected_result == get_possible_numbers(max_number, actual_input)
