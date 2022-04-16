N = int(input())

count = 0
divide_num = N // 2
while N != 0:
    if N < 4:
        break

    if divide_num ** 2 <= N:
        N -= (divide_num ** 2)
        count += 1
    else:
        divide_num -= 1

print(count + N)