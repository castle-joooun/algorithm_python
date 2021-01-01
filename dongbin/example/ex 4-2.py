h = int(input())
count = 0

for i in range(h+1):
    for j in range(60):
        for n in range(60):
            if '3' in str(i) + str(j) + str(n):
                count += 1

print(count)