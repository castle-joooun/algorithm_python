A, B = map(int, input().split())
m = int(input())
l = list(map(int, input().split()))

original_num = 0
for i in range(m - 1):
    original_num = (original_num + l[i]) * A
original_num += l[-1]

answer = []
while original_num:
    answer.append(original_num % B)
    original_num //= B
print(*answer[::-1])