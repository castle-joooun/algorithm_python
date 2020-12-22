d = [False for _ in range(10001)]

for i in range(1, 10000):
    num_str = str(i)
    l = []
    for s in num_str:
        l.append(int(s))

    idx = int(num_str)
    for j in range(len(l)):
        idx += l[j]

    if idx <= 10000:
        d[idx] = True

for i in range(1, 10000):
    if d[i] is False:
        print(i)