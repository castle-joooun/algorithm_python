N = int(input())
l = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(N)]

for i in range(N):
    # 왼쪽 검사
    for j in range(i):
        if l[i] > l[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
    # 오른쪽 검사
    right_i = (N - 1) - i
    for j in range(N - 1, right_i, -1):
        if l[right_i] > l[j]:
            dp[right_i][1] = max(dp[right_i][1], dp[j][1] + 1)

result = [sum(item) for item in dp]
print(max(result) + 1)
