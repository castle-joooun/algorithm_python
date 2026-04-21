n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
"""
n이 100인데, 최악의 경우 n번 반복할 수 있음으로 -> n^2

"""

while True:
    temp = []
    check = []

    for i in range(len(numbers)):
        if not check or check[-1] == numbers[i]:
            check.append(numbers[i])
        else:
            if not len(check) >= m:
                temp += check
            check = [numbers[i]]

    if check and not len(check) >= m:
        temp += check
    if len(temp) == len(numbers):
        break
    numbers = temp

print(len(numbers))
for x in numbers:
    print(x)