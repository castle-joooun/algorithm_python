num = int(input())
array = []
for _ in range(num):
    array.append(int(input()))

result = sorted(array, reverse=True)
for x in result:
    print(x, end=" ")