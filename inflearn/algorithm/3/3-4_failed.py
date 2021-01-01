n1 = int(input())
d1 = list(map(int, input().split()))
n2 = int(input())
d2 = list(map(int, input().split()))

d = d1 + d2
for x in sorted(d):
    print(x, end=' ')