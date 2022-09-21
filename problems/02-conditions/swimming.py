N, M, x, y = int(input()), int(input()), int(input()), int(input())

if N > M:
    x_dist = y
    y_dist = x
else:
    x_dist = x
    y_dist = y

if x_dist > N / 2:
    x_dist = N - x_dist
if y_dist > M / 2:
    y_dist = M - y_dist

if x_dist < y_dist:
    print(x_dist)
else:
    print(y_dist)
