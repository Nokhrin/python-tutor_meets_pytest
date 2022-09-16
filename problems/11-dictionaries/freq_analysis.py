"""
Дан текст: в первой строке записано количество строк в тексте, а затем сами строки.
Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте,
а при одинаковой частоте появления — в лексикографическом порядке.
"""

# collect and count words
lines_count = int(input())
words_dict = dict()
for i in range(lines_count):
    for word in input().split(sep=' '):
        words_dict[word] = words_dict.get(word, 0) + 1

# sorting for required output
count_words_list = []  # list of tuples
for word, count in words_dict.items():
    count_words_list.append((count, word))

count_words_list.sort(key=lambda x: (-x[0], x[1]))

for count_word_tuple in count_words_list:
    print(count_word_tuple[1])
