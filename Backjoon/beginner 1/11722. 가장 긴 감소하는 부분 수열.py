N = int(input())
d = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if d[i] < d[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
