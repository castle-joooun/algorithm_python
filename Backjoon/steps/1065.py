n = int(input())
result = 0

if n < 100:
    result += n
else:
    result += 99
    for i in range(100, 1001):
        if n < i:
            break

        d = []
        num_str = str(i)
        for s in num_str:
            d.append(int(s))

        num = d[0] - d[1]
        check = True
        for j in range(1, len(d) - 1):
            if d[j] - d[j + 1] != num:
                check = False
                break

        if check:
            result += 1

print(result)