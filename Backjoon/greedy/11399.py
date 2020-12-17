n = int(input())
d = list(map(int, input().split()))
result = 0

d.sort()
for i in range(n):
    sum = 0
    for j in range(i + 1):
        sum += d[j]
    result += sum

print(result)

