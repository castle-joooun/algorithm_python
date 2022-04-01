M, N = map(int, input().split())

check = [True] * (N + 1)
for i in range(2, N + 1):
    if check[i]:
        j = 2

        while (i * j) <= N:
            check[i * j] = False
            j += 1

for i in range(M, N + 1):
    if check[i]: print(i)
