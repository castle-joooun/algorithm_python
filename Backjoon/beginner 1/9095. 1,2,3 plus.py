import sys
input = sys.stdin.readline
dp = [0, 1, 2, 4]
for _ in range(int(input())):
    N = int(input())

    if len(dp) - 1 >= N:
        print(dp[N])
        continue
    for i in range(4, N + 1):
        if len(dp) - 1 < i:
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    print(dp[N])