import sys
from itertools import combinations

input = sys.stdin.readline

check = [False, False]
last_num = 1
decimals = []
while True:
    num = int(input())
    if num == 0:
        break

    if last_num < num:
        check += ([True] * (num - last_num))
        for i in range(last_num + 1, num + 1):
            if check[i]:
                j = 2

                while (i * j) <= num:
                    check[i * j] = False
                    j += 1

    decimals = list(set(decimals + [idx for (idx, value) in enumerate(check) if value]))
    check_decimals = combinations(decimals, 2)

    result = [(value[1] - value[0], value)
              for value in check_decimals
              if value[0] + value[1] == num]
    if len(result) == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        result.sort(key=lambda x: -x[0])
        print(f'{num} = {result[0][1][0]} + {result[0][1][1]}')
