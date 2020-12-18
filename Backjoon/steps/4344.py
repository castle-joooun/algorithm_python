for _ in range(int(input())):
    d = list(map(int, input().split()))
    avg = (sum(d) - d[0]) / d[0]
    count = 0
    for i in range(1, len(d)):
        if d[i] > avg:
            count += 1
    result = count / (len(d) - 1) * 100
    print('%0.3f' % result, end='')
    print('%')
