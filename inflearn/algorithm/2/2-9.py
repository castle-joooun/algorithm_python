n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

result = 0
for list in d:
    check = [0] * (6 + 1)
    money = 0
    for x in list:
        check[x] += 1
    idx = check.index(max(check))

    if check[idx] == 1:
        result = max(result, idx * 100)
    elif check[idx] == 2:
        result = max(result, 1000 + idx * 100)
    else:
        result = max(result, 10000 + idx * 1000)

print(result)