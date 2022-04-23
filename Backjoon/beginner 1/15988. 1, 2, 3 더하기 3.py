import sys
input = sys.stdin.readline

dp = [0] * 1_000_001
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(int(input())):
    N = int(input())

    for i in range(4, N + 1):
        if dp[i] != 0:
            continue

        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1_000_000_009

    print(dp[N])

