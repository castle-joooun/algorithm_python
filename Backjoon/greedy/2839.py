n = int(input())
count = int(1e9)

if n % 5 == 0:
    count = min(count, n // 5)
if n % 3 == 0:
    count = min(count, n // 3)

for i in range(1, n // 5 + 1):
    for j in range(1, n // 3 + 1):
        if n - (5 * i) - (3 * j) == 0:
            count = min(count, i + j)

