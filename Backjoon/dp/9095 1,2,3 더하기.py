n = int(input())
cache = [0] * 11
cache[1] = 1
cache[2] = 2
cache[3] = 4


def sol(n):
    if cache[n] != 0:
        return cache[n]

    for i in range(4, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]

    return cache[n]

for i in range(1, n + 1):
    k = int(input())
    print(sol(k))
