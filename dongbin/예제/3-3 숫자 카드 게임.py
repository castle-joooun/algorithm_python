n, m = map(int, input().split())

result = 0
for i in range(n):
    check = min(map(int, input().split()))
    result = max(check, result)

print(result)
