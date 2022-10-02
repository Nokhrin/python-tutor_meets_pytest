import pytest
from problems.dictionaries.access_rights import check_access


@pytest.mark.parametrize(
    argnames='actual_input, expected_output',
    argvalues=[
        (
                ['4', ['helloworld.exe R X', 'pinglog W R', 'nya R', 'goodluck X W R'],
                 '5', ['read nya', 'write helloworld.exe', 'execute nya', 'read pinglog', 'write pinglog']],
                ['OK', 'Access denied', 'Access denied', 'OK', 'OK']
        ),
        (
                ['1', ['abacaba X'],
                 '3', ['read abacaba', 'write abacaba', 'execute abacaba']],
                ['Access denied', 'Access denied', 'OK']
        ),
        (
                ['1', ['tmp_909925047 W X R'],
                 '7', ['execute tmp_909925047', 'read tmp_909925047', 'write tmp_909925047', 'read tmp_909925047', 'execute tmp_909925047', 'execute tmp_909925047', 'read tmp_909925047']],
                ['OK', 'OK', 'OK', 'OK', 'OK', 'OK', 'OK']
        ),
        (
                ['5', ['tmp_1017722015 W', 'tmp_897110090 X W R', 'tmp_651548400 W X', 'tmp_422551574 X R W', 'tmp_477658548 W'],
                 '1', ['write tmp_897110090']],
                ['OK']
        ),
        (
                ['2', ['tmp_584361681 R X', 'tmp_70361076 X'],
                 '3', ['read tmp_70361076', 'write tmp_70361076', 'write tmp_70361076']],
                ['Access denied', 'Access denied', 'Access denied']
        ),
        (
                ['4', ['tmp_796487715 X R W', 'tmp_31144126 X R', 'tmp_967334538 R', 'tmp_264755563 R W'],
                 '3', ['read tmp_264755563', 'execute tmp_796487715', 'execute tmp_796487715']],
                ['OK', 'OK', 'OK']
        ),
    ]
)
@pytest.mark.smoke
def test_check_access(actual_input, expected_output):
    """test response of check_access function"""
    files_count, names_and_access, requests_count, requests = actual_input
    assert expected_output == check_access(files_count, names_and_access, requests_count, requests)
