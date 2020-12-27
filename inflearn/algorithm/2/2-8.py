def reverse(x):
    result = 0
    while x > 0:
        result = result * 10 + (x % 10)
        x //= 10
    return result


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    else:
        return True


n = int(input())
d = list(map(int, input().split()))

for x in d:
    check = reverse(x)
    if isPrime(check):
        print(check, end=' ')