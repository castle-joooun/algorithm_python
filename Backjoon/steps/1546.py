n = int(input())
d = list(map(int, input().split()))
max_num = max(d)
result = 0

for x in d:
    result += x / max_num * 100
print(result / n)