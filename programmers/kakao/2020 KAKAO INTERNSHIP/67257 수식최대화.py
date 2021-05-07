import re
from itertools import permutations
import copy


def solution(expression):
    maximum = 0

    numbers = list(map(int, re.split("[-*+]", expression)))
    oper = re.split("[0-9]", expression)
    oper = ''.join(oper)

    for arr in list(permutations(['*', '-', '+'], 3)):
        numbers_temp = copy.deepcopy(numbers)
        oper_temp = copy.deepcopy(oper)

        for x in arr:
            while oper_temp.find(x) != -1:
                idx = oper_temp.find(x)

                temp = oper_temp[:idx]
                if idx != len(oper) - 1:
                    temp += oper_temp[idx + 1:]
                oper_temp = temp

                result = 0
                if x == '*':
                    result = numbers_temp[idx] * numbers_temp[idx + 1]
                elif x == '+':
                    result = numbers_temp[idx] + numbers_temp[idx + 1]
                else:
                    if numbers_temp[idx] > numbers_temp[idx + 1]:
                        result = numbers_temp[idx + 1] - numbers_temp[idx]
                    else:
                        result = numbers_temp[idx] - numbers_temp[idx + 1]

                del numbers_temp[idx + 1]
                del numbers_temp[idx]

                numbers_temp.insert(idx, result)

        maximum = max(maximum, abs(numbers_temp[0]))

    return maximum


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
print(list(permutations(['*', '-', '+'], 3)))
