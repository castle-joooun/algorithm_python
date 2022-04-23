import sys
input = sys.stdin.readline

N = int(input())
l = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [(-1, 10**8)] * (N + 1)
dp[0] = (-1, 0)
answer = []


for t in range(3):
    dp = [(-1, 10 ** 8)] * (N + 1)
    dp[0] = (-1, 0)
    dp[1] = (t, l[1][t])

    for i in range(2, N + 1):
        for j in range(3):
            if dp[i - 1][0] == j:
                continue

            check = dp[i][1]
            check = dp[i - 1][1]
            check = l[i][j]
            if dp[i][1] > dp[i - 1][1] + l[i][j]:
                dp[i] = (j, dp[i - 1][1] + l[i][j])

    answer.append(dp[N][1])

print(min(answer))
