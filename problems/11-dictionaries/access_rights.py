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
files_count = int(input())
files_settings = dict()
for i in range(files_count):
    full_input = input().split(sep=' ')
    files_settings[full_input[0]] = [setting for setting in full_input[1:]]

operations_count = int(input())
for i in range(operations_count):
    response = 'Access denied'
    operation, file_name = input().split(sep=' ')
    if operation == 'read':
        if 'R' in files_settings[file_name]:
            response = 'OK'
    elif operation == 'write':
        if 'W' in files_settings[file_name]:
            response = 'OK'
    elif operation == 'execute':
        if 'X' in files_settings[file_name]:
            response = 'OK'

    print(response)
