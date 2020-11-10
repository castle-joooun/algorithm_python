n, k = map(int, input().split())

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

for _ in range(k):
    min_index = array_a.index(min(array_a))
    max_index = array_b.index(max(array_b))

    array_a[min_index], array_b[max_index] = array_b[max_index], array_a[min_index]

print(sum(array_a))