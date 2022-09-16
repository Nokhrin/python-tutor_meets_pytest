"""
Улитка ползет по вертикальному шесту высотой h метров,
поднимаясь за день на a метров, а за ночь спускаясь на b метров.
На какой день улитка доползет до вершины шеста?

Программа получает на вход натуральные числа h, a, b.

Программа должна вывести одно натуральное число. Гарантируется, что a>b
"""

total_height, day_displacement, night_displacement = int(input()), int(input()), int(input())
whole_days_distance = total_height - day_displacement
one_day_displacement = day_displacement - night_displacement
# number of complete days of forward and back motion
# +
# 1 for day in which snail will approach finish line
# +
# 1 for last day, which was subtracted from whole_days_distance
total_days = (whole_days_distance // one_day_displacement) + \
             int(whole_days_distance % one_day_displacement != 0) + \
             1
print(total_days, end='')
