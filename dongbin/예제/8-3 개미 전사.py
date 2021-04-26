n = int(input())
data = list(map(int, input().split()))

d = [0] * 101
d[0], d[1] = data[0], max(data[0], data[1])

result = 0
for i in range(2, n):
    d[i] = max(data[i - 1], data[i] + d[i - 2])

print(max(d))
