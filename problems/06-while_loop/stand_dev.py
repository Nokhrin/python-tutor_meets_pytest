"""
Дана последовательность натуральных чисел x1, x2, ..., xn. Стандартным отклонением называется величина
σ=( ( (x1 − s) ** 2 + (x2 − s) ** 2 + … + (xn − s) ** 2 ) / (n−1) ) ** 0.5
где s = (x1 + x2 + … + xn) / n — среднее арифметическое последовательности.

Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
Разрешается использовать простые переменные и цикл while.
"""

# since we cannot use lists or any similar data type
# the standard deviation is the square root of the variance of X
# https://en.wikipedia.org/wiki/Standard_deviation#Definition_of_population_values
# which gives ( (total_squares * count - total * total) / (count * count) / (count - 1) ) ** 0.5

number = int(input())  # number entered
count = 0  # numbers count
total = 0  # total numbers sum
total_squares = 0  # total squared numbers sum

# read the input
while number != 0:
    count += 1
    total += number
    total_squares += number * number
    number = int(input())

variance = (total_squares - total * total / count) / (count - 1)
stand_dev = variance ** 0.5

print(stand_dev, end='')
