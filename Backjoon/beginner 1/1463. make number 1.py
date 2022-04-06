def make_one(N, result, cnt=0):
    if N == 1:
        return cnt
    if result <= cnt + 1:
        return 10**7

    if N % 3 == 0:
        result = min(make_one(N // 3, result, cnt + 1), result)
    if N % 2 == 0:
        result = min(make_one(N // 2, result, cnt + 1), result)
    if N > 1:
        result = min(make_one(N - 1, result, cnt + 1), result)

    return result


N = int(input())

print(make_one(N, 10**7))
