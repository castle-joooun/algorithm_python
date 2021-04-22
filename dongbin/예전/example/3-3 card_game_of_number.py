n, m = map(int, input().split())

d = [[] for i in range(n)]
min_list = []

for i in range(n):
    d[i] = map(int, input().split())
    min_list.append(min(d[i]))

print(max(min_list))