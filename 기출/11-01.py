n = int(input())
d = list(map(int, input().split()))
team = 0

d.sort()

while len(d) != 0:
    num = d[-1]
    d = d[:len(d) - num]
    team += 1

print(team)
