n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

div = n // 2
result = 0

for i in range(n):
    if i < div:
        result += sum(d[i][div - i:div + i + 1])
        #print(d[i][div - i:div + i + 1])
    if i == div:
        result += sum(d[i])
        #print(d[i])
    if i > div:
        result += sum(d[i][i - div:div - i])
        #print(d[i][i - div:div - i])

print(result)