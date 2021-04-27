k = int(input())


result = k // (10 ** (len(str(k)) - 1))
k %= (10 ** (len(str(k)) - 1))

while k != 0:
    num = k // (10 ** (len(str(k)) - 1))
    k %= (10 ** (len(str(k)) - 1))
    result = max(result + num, result * num)

print(result)
