import math

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(math.lcm(A, B))
