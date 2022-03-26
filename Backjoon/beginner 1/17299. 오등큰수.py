import collections

N = int(input())
l = list(map(int, input().split()))

answer = [-1] * N
count = collections.Counter(l)
stack = [0]

for i in range(1, N):
    while stack and count[l[stack[-1]]] < count[l[i]]:
        answer[stack.pop()] = l[i]
    stack.append(i)

print(*answer)
