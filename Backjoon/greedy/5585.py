money = 1000 - int(input())
d = [500, 100, 50, 10, 5, 1]
result = 0

for x in d:
    result += money // x
    money = money % x

print(result)