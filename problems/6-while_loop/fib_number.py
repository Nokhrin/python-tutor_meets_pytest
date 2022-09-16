search_num = int(input())
fib_num = 1
fib_index = 1
prev_num = 0

while fib_num != search_num:
    tmp = prev_num
    prev_num = fib_num
    fib_num = prev_num + tmp
    fib_index += 1
    if fib_num > search_num:
        fib_index = -1
        break

print(fib_index)
