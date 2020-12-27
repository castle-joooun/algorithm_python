import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = list(map(int, input().split()))

cnt = 1 if d[n - 1] == m else 0
for i in range(n - 1):
    check = d[i]
    for j in range(i + 1, n):
        check += d[j]
        if check == m:
            cnt += 1
            break
        elif check > m:
            break

print(cnt)