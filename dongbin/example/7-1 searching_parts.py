n = int(input())
array_n = list(map(int, input().split()))
m = int(input())
array_m = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# have to sort array when doing binary_search
array_n.sort()
for i in array_m:
    result = binary_search(array_n, i, 0, n - 1)
    if result is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')