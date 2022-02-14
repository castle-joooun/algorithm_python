N = int(input())

result = 0

for x in [5, 3]:
    result += N // x
    N %= x

if N != 0:
    print(-1)
else: 
    print(result)
