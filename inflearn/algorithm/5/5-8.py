n = int(input())
will = set([])
d = set([])
for i in range(n):
    will.add(input())
for i in range(n - 1):
    d.add(input())

print(list(will - d)[0])