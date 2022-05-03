N = int(input())
l = list(map(int, input().split()))
dp = [num for num in l]

for i in range(1, N):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + l[i])

print(max(dp))
