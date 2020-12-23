import sys
from itertools import combinations
#sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
d = list(map(int, input().split()))
mix = list(combinations(d, 3))
result = []

for x in mix:
    if sum(x) not in result:
        result.append(sum(x))
result.sort(reverse=True)
print(result[k - 1])