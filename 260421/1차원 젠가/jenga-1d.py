n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
"""
N이 100. 
"""

def check(s, e):
    temp = []
    for i in range(len(result)):
        if s - 1 <= i < e:
            continue
        temp.append(result[i])

    return temp

result = blocks[::]
result = check(s1, e1)
result = check(s2, e2)

print(len(result))
for x in result:
    print(x)