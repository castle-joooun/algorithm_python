N = int(input())
l = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
