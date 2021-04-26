n = int(input())
count = 0

while n != 1:
    if n % 5 == 0:
        n //= 5
    elif n % 3 == 0:
        n //= 3
    else:
        n -= 1
    count += 1

print(count)
