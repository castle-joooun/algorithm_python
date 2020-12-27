n = int(input())
d = list(input().split())
result = 0
idx = 0

for x in d:
    check = 0
    for num in x:
        check += int(num)
    if result < check:
        result = check
        idx = x

print(idx)