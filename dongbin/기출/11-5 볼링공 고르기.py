n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

check = [0] * (m + 1)
for x in arr:
    check[x] += 1

for i in range(1, len(check)):
    n -= check[i]
    result += check[i] * n

print(result)
