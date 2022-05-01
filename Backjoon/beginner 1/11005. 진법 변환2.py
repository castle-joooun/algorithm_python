temp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int, input().split())
answer = ''
while N:
    answer += str(temp[N % B])
    N //= B

print(answer[::-1])