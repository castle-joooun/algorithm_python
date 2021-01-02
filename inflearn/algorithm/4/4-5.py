import sys

input = sys.stdin.readline

n = int(input())
d = []

for _ in range(n):
    d.append(tuple(map(int, input().split())))

d.sort(key=lambda x: (x[1], x[0]))
end = 0
cnt = 0
for s, e in d:
    if s >= end:
        cnt += 1
        end = e
print(cnt)
