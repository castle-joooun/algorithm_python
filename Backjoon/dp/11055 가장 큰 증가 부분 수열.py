n = int(input())
d = list(map(int, input().split()))

dp = [x for x in d]

for i in range(1, n):
    temp = d[i]
    for j in range(i):
        if d[i] > d[j]:
            dp[i] = max(dp[i], d[i] + dp[j])
print(max(dp))
