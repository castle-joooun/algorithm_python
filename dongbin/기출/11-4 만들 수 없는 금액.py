k = input()
arr = list(map(int, input().split()))
arr.sort()

target = 1
for x in arr:
    if target < x:
        break
    target += x

print(target)
