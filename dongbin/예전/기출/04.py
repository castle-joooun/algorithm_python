n = int(input())
d = list(map(int, input().split()))
d.sort()

target = 1
for x in d:
    if target < x:
        break
    target += x

print(target)
