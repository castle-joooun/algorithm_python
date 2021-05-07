n = int(input())

dp = []
dp.append([1 for _ in range(10)])
for i in range(n):
    dp.append([0 for _ in range(10)])

for i in range(1, n):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]

print(sum(dp[n - 1]) % 10007)
