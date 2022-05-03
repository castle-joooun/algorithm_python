N = int(input())
l = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = l[0]

for i in range(2, N + 1):
    for j in range(i, 0, -1):
        if l[i - 1] > l[j - 1]:
            dp[i] = dp[j]
            break

    dp[i] += l[i - 1]

print(max(dp))
