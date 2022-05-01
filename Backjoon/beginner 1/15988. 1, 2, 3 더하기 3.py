import sys
input = sys.stdin.readline

T = int(input())
l = [int(input()) for _ in range(T)]

dp = [0] * (max(l) + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max(l) + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1_000_000_009

print(*[dp[N] for N in l], sep='\n')