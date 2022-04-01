from math import gcd
from itertools import combinations

for _ in range(int(input())):
    l = list(map(int, input().split()))
    n = l[0]
    l = l[1:]
    combinations_list = list(combinations(l, 2))

    result = [gcd(a, b) for a, b in combinations_list]
    print(sum(result))

