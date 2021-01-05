n = int(input())
d = dict()
for i in range(n):
    d[input()] = 1
for i in range(n - 1):
    d[input()] = 0
for key, val in d.items():
    if val == 1:
        print(key)
        break