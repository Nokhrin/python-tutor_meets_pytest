"""
Однажды, разбирая старые книги на чердаке, школьник Вася нашёл англо-латинский словарь.
Английский он к тому времени знал в совершенстве, и его мечтой было изучить латынь.
Поэтому попавшийся словарь был как раз кстати.
К сожалению, для полноценного изучения языка недостаточно только одного словаря:

кроме англо-латинского необходим латинско-английский.
За неимением лучшего он решил сделать второй словарь из первого.

Как известно, словарь состоит из переводимых слов,
к каждому из которых приводится несколько слов-переводов.

Для каждого латинского слова, встречающегося где-либо в словаре,
Вася предлагает найти все его переводы
(то есть все английские слова, для которых наше латинское встречалось в его списке переводов),
и считать их и только их переводами этого латинского слова.
Помогите Васе выполнить работу по созданию латинско-английского словаря из англо-латинского.


В первой строке содержится единственное целое число N — количество английских слов в словаре.
Далее следует N описаний.
Каждое описание содержится в отдельной строке,
в которой записано сначала английское слово, затем отделённый пробелами дефис,
затем разделённые запятыми с пробелами переводы этого английского слова на латинский.
Все слова состоят только из маленьких латинских букв.
Переводы отсортированы в лексикографическом порядке.
Порядок следования английских слов в словаре также лексикографический.

Выведите соответствующий данному латинско-английский словарь,
в точности соблюдая формат входных данных.
В частности, первым должен идти перевод лексикографически минимального латинского слова,
далее — второго в этом порядке и т.д.
Внутри перевода английские слова должны быть также отсортированы лексикографически.
"""
import re

definitions_count = int(input())
latins_set = set()
eng_latin_dict = dict()
latin_eng_dict = dict()

for i in range(definitions_count):
    input_list = re.split(' - |, ', input())  # split using regular expression
    eng_word = input_list[0]
    eng_latin_dict[eng_word] = set(latin for latin in input_list[1:])
    latins_set.update(set(latin for latin in input_list[1:]))

for latin in sorted(list(latins_set)):
    latin_eng_dict[latin] = []
    for eng_word in eng_latin_dict:
        if latin in eng_latin_dict[eng_word]:
            latin_eng_dict[latin].append(eng_word)
    latin_eng_dict[latin].sort()

print(len(latin_eng_dict))
for latin in sorted(latin_eng_dict.keys()):
    print(latin, '-', ', '.join(latin_eng_dict[latin]))
