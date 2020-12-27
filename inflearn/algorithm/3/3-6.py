n = int(input())
d = []

result = 0
for i in range(n):
    d.append(list(map(int, input().split())))
    result = max(result, sum(d[i]))

cross1 = 0
cross2 = 0
for i in range(n):
    check = 0
    for j in range(n):
        check += d[j][i]
        if i == j:
            cross1 += d[i][j]
        if j + i == n - 1:
            cross2 += d[i][j]
    result = max(result, check)
result = max(result, cross1, cross2)
print(result)
