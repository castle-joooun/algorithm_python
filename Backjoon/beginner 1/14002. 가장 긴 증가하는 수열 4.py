N = int(input())
l = list(map(int, input().split()))
dp = [1] * N
arr = [[num] for num in l]

for i in range(1, N):
    for j in range(i):
        if l[i] > l[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            arr[i] = arr[j] + [l[i]]

print(max(dp))
for x in arr:
    if len(x) == max(dp):
        print(*x)