N = int(input())

result = 987654321

for x in range(1, N // 5 + 1):
    temp = 0
    n = N

    temp += x
    n -= (5 * x)

    temp += (n // 3)
    n %= 3

    if n == 0:
        result = min(temp, result)

if N % 3 == 0:
    result = min(result, N // 3)

if N == 987654321:
    print(-1)
else: 
    print(result)
