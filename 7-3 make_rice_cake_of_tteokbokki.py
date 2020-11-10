n, m = map(int, input().split())
arr = list(map(int, input().split()))
value = []


def binary_search(array, h, start, end):
    mid = (start + end) // 2

    if start >= end:
        return

    sum = 0
    for x in array:
        if x > mid:
            sum += (x - mid)

    if sum >= h:
        value.append(mid)
        binary_search(array, h, mid + 1, end)
    else:
        binary_search(array, h, start, mid - 1)


binary_search(arr, m, 1, max(arr))
print(max(value))