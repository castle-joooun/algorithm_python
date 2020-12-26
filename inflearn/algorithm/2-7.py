import math

n = int(input())
d = [True for _ in range(n + 1)]
result = 0

for i in range(2, int(math.sqrt(n)) + 1):
    if d[i]:
        j = 2
        while i * j <= n:
            d[i * j] = False
            j += 1

for i in range(2, len(d)):
    if d[i]:
        result += 1

print(result)