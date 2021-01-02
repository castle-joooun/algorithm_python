n = int(input())
d = list(map(int, input().split()))

lt = 0
rt = n - 1
cnt = 0
str_sort = ''
big = []
large = 0
while lt <= rt:
    if d[lt] > large:
        big.append((d[lt], 'L'))
    if d[rt] > large:
        big.append((d[rt], 'R'))
    big.sort()
    if len(big) == 0:
        break
    else:
        if big[0][1] == 'L':
            str_sort += 'L'
            lt += 1
        else:
            str_sort += 'R'
            rt -= 1
        large = big[0][0]
        cnt += 1
    big.clear()
print(cnt)
print(str_sort)