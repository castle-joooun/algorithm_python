n, m = map(int, input().split())
data = list(map(int, input().split()))

cut = max(data)
dduck = 0

while m > dduck:
    dduck = 0
    cut -= 1

    for x in data:
        if x > cut:
            dduck += x - cut

print(cut)
