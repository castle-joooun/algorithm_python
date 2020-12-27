n = int(input())
d = [input().lower() for _ in range(n)]

for i in range(n):
    reverse = ''
    for char in d[i]:
        reverse = char + reverse

    print('#%d' %(i + 1), end=' ')
    if reverse == d[i]:
        print('YES')
    else:
        print('NO')
