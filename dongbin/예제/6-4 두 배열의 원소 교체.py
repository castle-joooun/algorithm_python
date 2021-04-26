n, k = map(int, input().split())
d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))

for _ in range(k):
    min_idx = d1.index(min(d1))
    max_idx = d2.index(max(d2))

    if d1[min_idx] >= d2[max_idx]:
        continue
    d1[min_idx], d2[max_idx] = d2[max_idx], d1[min_idx]

print(sum(d1))
