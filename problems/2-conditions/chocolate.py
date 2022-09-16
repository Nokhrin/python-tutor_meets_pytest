n, m, k = int(input()), int(input()), int(input())
if ((n == 1 and m >= k) or (m == 1 and n >= k)) or (n > 1 and m > 1 and (k % m == 0 or k % n == 0) and n * m >= k):
    print('YES')
else:
    print('NO')
