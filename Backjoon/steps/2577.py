a = int(input())
b = int(input())
c = int(input())
count = [0 for _ in range(10)]

multiple = str(a * b * c)
for i in range(len(multiple)):
    count[int(multiple[i])] += 1

for x in count:
    print(x)