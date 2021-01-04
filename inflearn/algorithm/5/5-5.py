n, k = map(int, input().split())
d = [i for i in range(1, n + 1)]

check = 0
while len(d) > 1:
    check += k
    while check > len(d):
        check -= len(d)
    check -= 1
    del d[check]
print(d[0])