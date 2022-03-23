N, K = map(int, input().split())

visited = [False for _ in range(N)]
result = []
index = 1

while False in visited:
    count = 1
    while True:
        if index > N:
            index -= N

        if count == 3 and not visited[index - 1]:
            result.append(str(index))
            visited[index - 1] = True
            index += 1
            break
        else:
            if visited[index - 1]:
                index += 1
                continue

            count += 1
            index += 1

print(f'<{", ".join(result)}>')
