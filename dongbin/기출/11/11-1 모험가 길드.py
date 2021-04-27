k = int(input())
arr = list(map(int, input().split()))

result = 0
arr.sort()

while len(arr) != 0:
    check = arr.pop()
    for i in range(check - 1):
        if len(arr) == 0:
            break
        arr.pop()
    else:
        result += 1

print(result)
