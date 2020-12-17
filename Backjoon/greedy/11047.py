n, k = map(int, input().split())
d = []
result = 0

for _ in range(n):
    d.append(int(input()))
d.sort(reverse= True)

for x in d:
    while k // x > 0:
        result += k // x
        k = k % x

print(result)