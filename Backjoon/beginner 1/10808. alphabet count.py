S = input()

result = {}
for i in range(ord('a'), ord('z') + 1):
    result[chr(i)] = 0

for char in S:
    result[char] += 1

print(*result.values())
