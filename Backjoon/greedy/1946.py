import sys

for _ in range(int(input())):
    result = 0
    d = []
    for i in range(int(input())):
        a, b = map(int, sys.stdin.readline().split())
        d.append([a, b])

    fire = []
    for i in range(len(d)):
        for j in range(len(d)):
            if i != j and (d[i][0] > d[j][0] and d[i][1] > d[j][1]):
                if d[i] not in fire:
                    fire.append(d[i])
    result = len(d) - len(fire)
    print(result)