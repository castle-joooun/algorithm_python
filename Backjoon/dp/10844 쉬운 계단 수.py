n = int(input())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = i * 9

print(dp[n])
