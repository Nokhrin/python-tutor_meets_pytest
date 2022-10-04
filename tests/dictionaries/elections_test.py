import pytest
from problems.dictionaries.elections import count_voices


@pytest.mark.parametrize(
    argnames='actual_input, expected_result',
    argvalues=[
        (['5', ['McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1']], ['McCain 16', 'Obama 17']),
        (['13',
          ['McCain 10', 'McCain 3', 'Obama 19', 'Obama 2', 'McCain 7', 'McCain 2', 'Obama 6', 'Obama 10', 'McCain 11',
           'McCain 5', 'Obama 3', 'Obama 12', 'McCain 13']], ['McCain 51', 'Obama 52']),
        (['1', ['Obama 1']], ['Obama 1']),
        pytest.param(['1', ['Obama 1']], [], marks=pytest.mark.xfail(reason='result should be empty', strict=True)),
        (['7', ['ivan 2', 'gena 1', 'sergey 100000', 'ivan 1', 'ivan 1', 'ivan 0', 'gena 100']],
         ['gena 101', 'ivan 4', 'sergey 100000']),
        (['61',
          ['Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1',
           'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1',
           'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1',
           'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1',
           'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1',
           'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1', 'Obama 1',
           'McCain 59']], ['McCain 59', 'Obama 60']),
    ]
)
@pytest.mark.smoke
def test_count_voices(actual_input, expected_result):
    """Test output of count_voices."""
    assert expected_result == count_voices(actual_input[0], actual_input[1])


@pytest.mark.parametrize(
    argnames='actual_input',
    argvalues=[
        ('5', ['McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1']),
    ]
)
@pytest.mark.filterwarnings('some warning from pytest')
def test_entries_count(actual_input):
    """Test expected and actual amount of input strings"""
    assert int(actual_input[0]) == len(actual_input[1]), 'Actual amount of strings is not equal to expected'
