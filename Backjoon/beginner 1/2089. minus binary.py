N = int(input())

if N == 0:
    print(0)
    exit()

result = ''
while N != 0:
    if N % -2:
        N = N // -2 + 1
        result = '1' + result
    else:
        N //= -2
        result = '0' + result

print(result)