n = int(input())
data = []

for _ in range(n):
    x, a = input().split()
    data.append((x, int(a)))


def setting(d):
    return d[1]


data.sort(key=setting)

for x in data:
    print(x[0], end=" ")
