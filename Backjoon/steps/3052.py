d = [int(input()) % 42 for _ in range(10)]
result = []

for x in d:
    if x in result:
        continue
    result.append(x)

print(len(result))