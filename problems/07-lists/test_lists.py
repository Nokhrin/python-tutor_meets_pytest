import pytest


@pytest.mark.skip(reason='checking another problem')
@pytest.mark.parametrize(
    'str_input, str_correct_output',
    [
        ('-1 2 3 -1 -2', '2 3'),
        ('1 -3 4 -2 1', ''),
        ('1 -1 1 -1 -1 1 -1 1 -1 1', '-1 -1'),
        ('1 -1 1 -1 1', ''),
        ('1 2 3 4', '1 2')
    ]
)
def test_lists_4(str_input, str_correct_output):
    numbers_list = [int(str_num) for str_num in str_input.split(sep=' ')]
    first_two_same_sign = []
    for i in range(1, len(numbers_list)):
        prev_element = numbers_list[i - 1]
        curr_element = numbers_list[i]
        if prev_element * curr_element > 0:
            first_two_same_sign = [str(prev_element), str(curr_element)]
            break

    str_output = ' '.join(first_two_same_sign)
    assert str_output == str_correct_output


@pytest.mark.parametrize(
    argnames='str_input, correct_output',
    argvalues=[
        ('1 2 3 4 5', '0'),
        ('5 4 3 2 1', '0'),
        ('1 5 1 5 1', '2'),
        ('5 1 5 1 5', '1'),
        ('5 5 5 5 5', '0'),
        ('345354', '0'),
        ('2147483647 0 1 2 3', '0')
    ]
)
def test_lists_5(str_input, correct_output):
    numbers_list = [int(str_numbers) for str_numbers in str_input.split(sep=' ')]
    greatest_count = 0
    for number_index in range(1, len(numbers_list) - 1):
        previous_number = numbers_list[number_index - 1]
        current_number = numbers_list[number_index]
        next_number = numbers_list[number_index + 1]
        if current_number > previous_number and current_number > next_number:
            greatest_count += 1
    greatest_count = str(greatest_count)
    assert greatest_count == correct_output
