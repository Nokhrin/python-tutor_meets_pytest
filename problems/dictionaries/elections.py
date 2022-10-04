"""
Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования.
Сначала проводятся выборы в каждом штате и определяется победитель выборов в данном штате.
Затем проводятся государственные выборы: на этих выборах каждый штат имеет определенное число голосов —
число выборщиков от этого штата.
На практике, все выборщики от штата голосуют в соответствии с результами голосования внутри штата,
то есть на заключительной стадии выборов в голосовании участвуют штаты, имеющие различное число голосов.

В первой строке дано количество записей.
Далее, каждая запись содержит фамилию кандидата и число голосов, отданных за него в одном из штатов.
Подведите итоги выборов:
для каждого из участника голосования определите число отданных за него голосов.
Участников нужно выводить в алфавитном порядке.
"""

def count_voices(total_records: str, name_voices: str) -> list:
    """
    Count voices for each candidate.

    :param total_records: expected number of entries with lastname and voices
    :param name_voices: strings with lastname and voices
    :return: list of strings <lastname> <total voices>
    """

    total_records = int(total_records)
    candidates_votes_dict = {}
    for i in range(total_records):
        name_votes = name_voices[i].split(sep=' ')
        name, votes = name_votes[0], int(name_votes[1])
        if name in candidates_votes_dict.keys():
            candidates_votes_dict[name] += votes
        else:
            candidates_votes_dict[name] = votes

    result_list = []
    for name in sorted(list(candidates_votes_dict.keys())):
        result_list.append(f'{name} {str(candidates_votes_dict[name])}')

    return result_list
