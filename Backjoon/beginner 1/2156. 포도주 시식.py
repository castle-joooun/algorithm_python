import sys
input = sys.stdin.readline

N = int(input())
l = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
if N == 1:
    print(l[1])
elif N == 2:
    print(l[1] + l[2])
else:
    dp[1] = (1, l[1])
    dp[2] = (2, l[1] + l[2])
    for i in range(3, N + 1):
        check1 = check2 = (0, 0)
        if dp[i - 1][0] < 2:
            check1 = (dp[i - 1][0] + 1, dp[i - 1][1] + l[i])
        check2 = (0, dp[i - 1][1])

        dp[i] = check1 if check1[1] > check2[1] else check2

    print(dp[N][1])
