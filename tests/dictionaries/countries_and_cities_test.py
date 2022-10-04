import pytest
from problems.dictionaries.countries_and_cities import get_country_for_city


@pytest.mark.parametrize(
    argnames='actual_input, requests, expected_result',
    argvalues=[
        pytest.param(['2', ['Russia Moscow Petersburg Novgorod Kaluga', 'Ukraine Kiev Donetsk Odessa']],
                     ['3', ['Odessa', 'Moscow', 'Novgorod']],
                     ['Ukraine', 'Russia', 'Russia'], id='Odessa, Moscow, Novgorod'),
        (['5', ['A B', 'C D', 'E F', 'G H', 'I J']], ['5', ['J', 'H', 'F', 'D', 'B']], ['I', 'G', 'E', 'C', 'A']),
        (['5', ['A B', 'C D E', 'F G H I', 'J K L M N', 'O P Q R S T']], ['15', ['T', 'S', 'N', 'R', 'M', 'I', 'Q', 'L', 'H', 'E', 'P', 'K', 'G', 'D', 'B']], ['O', 'O', 'J', 'O', 'J', 'F', 'O', 'J', 'F', 'C', 'O', 'J', 'F', 'C', 'A']),
        (['3', ['JNHIZN5VT5F0P NWKLYHJLJ7S5I 55SZACOU8GZC0E QSRASODSSZ4CJ', 'E61OETO7GT 2ORRX8WBTML JLY3T2PZEY35KM 9N5BIXINMS9YL', 'IK59912BIG MC0L2E4P2C U0M42ZG6I40 9XW44CTBJB4']], ['9', ['NWKLYHJLJ7S5I', '9XW44CTBJB4', '2ORRX8WBTML', '9N5BIXINMS9YL', 'MC0L2E4P2C', 'U0M42ZG6I40', 'QSRASODSSZ4CJ', 'JLY3T2PZEY35KM', '55SZACOU8GZC0E']], ['JNHIZN5VT5F0P', 'IK59912BIG', 'E61OETO7GT', 'E61OETO7GT', 'IK59912BIG', 'IK59912BIG', 'JNHIZN5VT5F0P', 'E61OETO7GT', 'JNHIZN5VT5F0P']),
    ]
)
def test_countries_and_cities(actual_input, requests, expected_result):
    """Tests output of countries_and_cities."""
    actual_result = get_country_for_city(actual_input[0], actual_input[1],
                                         requests[0], requests[1])
    assert expected_result == actual_result
