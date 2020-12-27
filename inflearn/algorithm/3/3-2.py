s = input()
num = 0

for x in s:
    if '0' <= x <= '9':
        num = num * 10 + int(x)

print(num)

cnt = 0
for n in range(1, num // 2 + 1):
    if num % n == 0:
        cnt += 1

print(cnt + 1)