n = int(input())
d = []
for _ in range(n):
    d.append(tuple(map(int, input().split())))

d.sort(reverse=True)
cm = 0
kg = 0
cnt = 0
for h, w in d:
    if h > cm or w > kg:
        cm = max(cm, h)
        kg = max(kg, w)
        cnt += 1

print(cnt)