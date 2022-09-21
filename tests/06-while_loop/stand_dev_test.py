import pytest


@pytest.mark.parametrize(
    argnames='numbers_list, expected_stand_dev',
    argvalues=[
        ([1, 7, 9, 0], 4.16333199893),
        ([1, 2, 3, 0], 1.0),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 0.0),
        ([3, 9, 5, 2, 0], 3.09569593683),
        ([10, 1, 1, 1, 1, 1, 0], 3.67423461417),
        ([58, 12, 51, 27, 79, 5, 44, 9, 86, 13, 0], 29.70297403740),
        ([51, 86, 7, 2, 75, 64, 23, 3, 25, 34, 62, 93, 41, 15, 96, 62, 58, 41, 43, 89, 0], 30.19149409667)
    ]
)
def test_stand_dev(numbers_list, expected_stand_dev):
    count = 0  # numbers count
    total = 0  # total numbers sum
    total_squares = 0  # total squared numbers sum

    for number in numbers_list:
        # read the input
        if number == 0:
            break
        else:
            count += 1
            total += number
            total_squares += number * number

    variance = (total_squares - total * total / count) / (count - 1)
    stand_dev = variance ** 0.5

    assert round(stand_dev, 11) == expected_stand_dev
