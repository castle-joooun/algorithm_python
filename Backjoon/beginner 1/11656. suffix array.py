s = input()

result = [s]
for i in range(1, len(s)):
    result.append(s[i:])

for x in sorted(result):
    print(x)
