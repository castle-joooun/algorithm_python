import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
d = list(map(int, input().split()))
avg = round(sum(d) / len(d), 1)
idx = []
i = 0

while True:
    if avg + i in d:
        idx.append(d.find(avg + i))
    if avg - i in d and i != 0:
        idx.append(d.find(avg - i))
