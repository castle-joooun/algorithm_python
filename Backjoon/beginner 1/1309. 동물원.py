N = int(input())
dp = [1] * (N + 1)
dp[1] = 3

if N == 1:
    print(dp[N])
else:
    for i in range(2, N + 1):
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9_901
    print(dp[N])