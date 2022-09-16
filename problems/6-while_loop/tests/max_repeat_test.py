import pytest


@pytest.mark.parametrize(
    argnames='input_numbers, max_count_expected',
    argvalues=[
        ('177910', 2),
        ('6', 0),
        ('444444444444444', 15)
    ]
)
def test_max_repeat(input_numbers, max_count_expected):
    curr_count = 0
    max_count = 0
    curr_number = input_numbers[0]  # initial value
    prev_number = None

    for str_number in input_numbers[1:]:
        while curr_number != 0:
            if curr_number == prev_number or prev_number is None:
                curr_count += 1
            else:
                curr_count = 1
            if curr_count > max_count:
                max_count = curr_count
            prev_number = curr_number
            curr_number = int(str_number)
    assert max_count_expected == max_count

"""
1
7
7
9
1
0

	

2

1
2
3
4
5
6
7
8
9
10
11
0

	

1

'4', '4', 4, 4 ,
'444444444444444', 15
4
4
4
4
4
4
4
4
4
4
0

	

15

6
0

	

1

1
2
3
2
3
3
2
4
4
4
4
2
3
3
3
2
2
3
0

	

4

1
2
2
1
2
1
2
1
2
0

	

2

1
2
2
0

	

2

2
2
1
0

	

2

1
2
3
3
2
2
4
4
4
4
4
5
5
5
6
3
3
3
3
3
3
5
5
5
5
3
3
3
4
5
5
5
0

	

6

1
2
1
1
1
2
0

	

3

2
1
1
1
1
2
1
0

	

4

"""