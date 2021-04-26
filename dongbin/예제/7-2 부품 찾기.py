n = int(input())
array = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))


def b_s(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for x in data:
    check = b_s(array, x, 0, len(array) - 1)

    if check == None:
        print('no', end=" ")
    else:
        print('yes', end=" ")
