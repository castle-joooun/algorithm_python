for _ in range(int(input())):
    n, s = input().split()
    n = int(n)
    result = ''

    for x in s:
        result += x * n

    print(result)
