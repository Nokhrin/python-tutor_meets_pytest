from math import ceil

interest, rub, kop = int(input()), int(input()), int(input())
total_kop = rub * 100 + kop
total_year_after = round((1 + interest / 100) * total_kop)
print(total_year_after)
rub_year_after = total_year_after // 100
kop_year_after = total_year_after % 100

print(rub_year_after, kop_year_after)
print(type(rub_year_after), type(kop_year_after))
print(int(rub_year_after), int(kop_year_after))
# print(int(round(rub_year_after, 0)), int(round(kop_year_after, 0)))
