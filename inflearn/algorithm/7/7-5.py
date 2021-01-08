def dfs(idx):
    global step
    if idx == n:
        if step > max(people) - min(people):
            check = set()
            for x in people:
                check.add(x)
            if len(check) == 3:
                step = max(people) - min(people)
    else:
        for i in range(3):
            people[i] += d[idx]
            dfs(idx + 1)
            people[i] -= d[idx]


n = int(input())
d = []
for _ in range(n):
    d.append(int(input()))

people = [0] * 3
step = 1e9
dfs(0)
print(step)