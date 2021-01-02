l = int(input())
d = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    d.sort()
    d[0] += 1
    d[-1] -= 1

print(max(d) - min(d))
