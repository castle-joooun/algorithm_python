n = int(input())
d = list(map(int, input().split()))

result = [0] * n
for i in range(n):
    check = d[i]
    j = 0
    while j != check:
        if result[j] != 0 and result[j] < i + 1:
            check += 1
        j += 1
    while True:
        if result[check] != 0:
            check += 1
        else:
            break
    result[check] = i + 1

for x in result:
    print(x, end=' ')