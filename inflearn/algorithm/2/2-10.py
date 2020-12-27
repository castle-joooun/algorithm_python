n = int(input())
d = list(map(int, input().split()))

result = 0
score = 1
for x in d:
    if x == 1:
        result += score
        score += 1
    else:
        score = 1

print(result)