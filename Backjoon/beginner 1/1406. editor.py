import sys

input = sys.stdin.readline

st1 = list(input().strip())
st2 = []

for _ in range(int(input())):
    order = tuple(input().split())

    if order[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif order[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif order[0] == 'B':
        if st1:
            st1.pop()
    elif order[0] == 'P':
        st1.append(order[1])

st1.extend(reversed(st2))
print(''.join(st1))
