N = int(input())
l = list(map(int, input().split()))

check = [1] * (max(l) + 1)
check[0] = check[1] = 0

for i in range(2, max(l) + 1):
    if check[i]:
        j = 2

        while (i * j) <= max(l):
            check[i * j] = 0
            j += 1

result = 0
for x in l:
    if check[x]:
        result += 1

print(result)