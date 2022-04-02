import sys, copy
input = sys.stdin.readline

N, Q = map(int, input().split())
l = [] + list(map(int, input().split()))

node = [] + [[False] * N for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    node[A - 1][B - 1] = node[B - 1][A - 1] = True

play = [list(map(int, input().split())) for _ in range(Q)]

for i in range(Q):
    copy_node = copy.deepcopy(node)
    start, end = play[i]
    next_road = start - 1
    result = ''
    while next_road != end - 1:
        result += str(l[next_road])
        for idx, check in enumerate(copy_node[next_road]):
            if check:
                copy_node[next_road][idx] = copy_node[idx][next_road] = False
                next_road = idx
                break

    print(int(result + str(l[end - 1])) % 1000000007)