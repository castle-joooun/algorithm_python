n = int(input())
count = 0
trans_num = n

while True:
    count += 1
    num = n // 10 + n % 10
    n = (n % 10) * 10 + num % 10
    if n == trans_num:
        break

print(count)