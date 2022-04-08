K = int(input())
P = [0] + list(map(int, input().split()))
dp = [0] * (K + 1)
dp[1] = P[1]

for i in range(2, K + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + P[j])

print(dp[K])

