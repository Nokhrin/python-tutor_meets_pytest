a = float(input())

# 2
# whole_hours = a * 12 // 360
# hours_tail = a * 12 % 360  # == minutes angle
# print(hours_tail)


# 3
H = a * 12 // 360
M = a * 12 % 360 * 60 // 360
S = a * 12 % 360 * 60 % 360 * 60 // 360
print(int(H), int(M), int(S))
