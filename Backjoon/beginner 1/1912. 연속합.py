N = int(input())
l = list(map(int, input().split()))
dp = [s for s in l]

for i in range(1, N):
    dp[i] = max(dp[i - 1] + dp[i], dp[i])

print(max(dp))
