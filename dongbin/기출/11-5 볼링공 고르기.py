n, m = map(int, input().split())
data = list(map(int, input().split()))

d = [0] * (max(data) + 1)

for x in data:
    d[x] += 1

result = 0
for i in range(1, len(d)):
    n -= d[i]
    result += d[i] * n

print(result)
