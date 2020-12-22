n = int(input())
num = int(input())
result = 0

for i in range(n):
    result += num % 10
    num //= 10

print(result)
