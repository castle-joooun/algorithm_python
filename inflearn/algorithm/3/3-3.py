def reverse(x, d):
    a, b = x
    check = d[a:b+1]
    for i in range(len(check) // 2):
        temp = check[i]
        check[i] = check[-(i + 1)]
        check[-(i + 1)] = temp
    d = d[:a] + check + d[b+1:]
    return d


list_re = [tuple(map(int, input().split())) for _ in range(10)]
d = [i for i in range(21)]

for x in list_re:
    d = reverse(x, d)

for i in range(1, 21):
    print(d[i], end=' ')