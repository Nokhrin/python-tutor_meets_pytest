import pytest

data_to_try = (
    ('10 3', ['8 10', '2 5', '3 6'], 'I.....I...'),
    ('5 2', ['1 2', '4 4'], '..I.I')
)
data_ids = ['{}, {}, {}'.format(data[0], data[1], data[2]) for data in data_to_try]


@pytest.mark.parametrize(
    argnames='setup_input, shots_input, expected_result',
    argvalues=data_to_try,
    ids=data_ids
)
def test_bowling(setup_input, shots_input, expected_result):
    pins, shots = [int(number) for number in setup_input.split(sep=' ')]
    pins_list = ['I'] * pins

    for i in range(shots):  # read input for each shot
        left, right = [int(position) for position in shots_input[i].split(sep=' ')]
        for j in range(left - 1, right):
            pins_list[j] = '.'

    pins_str = ''.join(pins_list)

    assert pins_str == expected_result


"""
10 3
8 10
2 5
3 6



I.....I...

5 2
1 2
4 4



..I.I

10 3
3 5
4 6
10 10



II....III.

5 0



IIIII

5 5
5 5
3 3
1 1
2 2
4 4



.....

20 1
1 20



....................

20 3
3 8
13 17
6 9



II.......III.....III

15 4
1 1
1 4
6 8
7 9



....I....IIIIII
"""
