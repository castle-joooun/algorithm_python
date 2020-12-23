import sys
# sys.stdin = open("input.txt", "rt")

for i in range(int(input())):
    n, s, e, k = map(int, input().split())
    d = list(map(int, input().split()))
    d = sorted(d[s - 1:e])
    print("#%d %d" % (i + 1, d[k - 1]))
