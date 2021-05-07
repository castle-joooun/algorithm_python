n = int(input())
d = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    check = []
    for j in range(i):
        if d[i] < d[j]:
            check.append(dp[j])

    if not check:
        continue
    dp[i] += max(check)

print(max(dp))
