from sys import stdin

input = stdin.readline

s = input().strip()
strs = []
for char in s:
    if char.isalnum():
        strs.append(char.lower())

for i in range(len(strs) // 2):
    if strs[i] != strs[(i + 1) * -1]:
        print(False)
        break
else:
    print(True)