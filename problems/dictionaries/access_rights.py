"""
В файловую систему одного суперкомпьютера проник вирус,
который сломал контроль за правами доступа к файлам.
Для каждого файла известно, с какими действиями можно к нему обращаться:
    запись W,
    чтение R,
    запуск X.

В первой строке содержится число N — количество файлов содержащихся в данной файловой системе.
В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами.
Далее указано чиcло M — количество запросов к файлам.
В последних M строках указан запрос вида Операция Файл.
К одному и тому же файлу может быть применено любое колличество запросов.

Вам требуется восстановить контроль над правами доступа к файлам
(ваша программа для каждого запроса должна будет возвращать OK
если над файлом выполняется допустимая операция,
или же Access denied, если операция недопустима.
"""


def check_access(files_count: str, names_and_access: list, requests_count: str, requests: list) -> list:
    """
    :param files_count: number of files in system
    :param names_and_access: list of <files_count> strings <filename> <access rights>
    :param requests_count: number of requests
    :param requests: list of <requests_count> strings <operation> <filename>
    :return: list of <requests_count> strings: <OK> for acceptable operation, <Access denied> otherwise
    """

    files_count = int(files_count)
    files_settings = dict()
    for i in range(files_count):
        full_input = names_and_access[i].split(sep=' ')
        files_settings[full_input[0]] = [setting for setting in full_input[1:]]

    operations_count = int(requests_count)
    response_list = []
    for i in range(operations_count):
        response = 'Access denied'
        operation, file_name = requests[i].split(sep=' ')
        if operation == 'read':
            if 'R' in files_settings[file_name]:
                response = 'OK'
        elif operation == 'write':
            if 'W' in files_settings[file_name]:
                response = 'OK'
        elif operation == 'execute':
            if 'X' in files_settings[file_name]:
                response = 'OK'

        response_list.append(response)

    return response_list
