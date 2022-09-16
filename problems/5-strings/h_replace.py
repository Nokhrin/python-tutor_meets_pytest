"""
Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
"""

str_input = input()

first_h_index = str_input.find('h')
last_h_index = str_input.rfind('h')

str_replace = str_input[first_h_index + 1 : last_h_index].replace('h', 'H')

str_new = str_input[:first_h_index + 1] + str_replace + str_input[last_h_index:]
print(str_new)


# In the hole in the ground there lived a hobbit
assert str_new == 'In the Hole in tHe ground tHere lived a hobbit'
