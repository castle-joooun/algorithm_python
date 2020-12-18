def self_number(num):
    d = [False for _ in range(num + 1)]
    d[0] = True
    i = 0
    while True:
        i += 1
        idx = i + (i // 10) + (i % 10)
        if idx > num:
            break
        d[idx] = True

    for j in range(num + 1):
        if d[j] is False:
            print(j)

self_number(10000)