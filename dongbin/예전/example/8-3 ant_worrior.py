n = int(input())
x = list(map(int, input().split()))
d = [0] * 100

d[0] = x[0]
d[1] = max(x[0], x[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + x[i])

print(d[n - 1])