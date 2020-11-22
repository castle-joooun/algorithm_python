n = int(input())
d = list(map(int, input().split()))

check = [False] * 1001
check[0] = True

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            check[d[i - 1] + d[j - 1]] = True
    check[i] = True

for i in range(len(check)):
    if not(check[i]):
        print(i)
        break
