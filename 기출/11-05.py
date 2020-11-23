n, m = map(int, input().split())
d = list(map(int, input().split()))

sum = 0

for i in range(n):
    for j in range(i + 1, n):
        if d[i] != d[j]:
            sum += 1

print(sum)