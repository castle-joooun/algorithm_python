N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]

result = []
index = 0

for _ in range(N):
    index += K - 1
    if index >= len(arr):
        index %= len(arr)

    result.append(str(arr.pop(index)))

print(f'<{", ".join(result)}>')
