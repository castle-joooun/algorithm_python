temp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = input().split()
answer = 0
B = int(B)
while N:
    value = temp.find(N[0])
    N = N[1:]
    if not N:
        answer += value
    else:
        answer = (answer + value) * B

print(answer)