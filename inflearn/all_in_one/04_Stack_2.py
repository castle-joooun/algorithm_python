"""
https://leetcode.com/problems/daily-temperatures/submissions/

739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""


def temperatures(temp):
    answer = [0] * len(temp)
    stack = []

    for cur_day, cur_temp in enumerate(temp):
        while stack and cur_temp > stack[-1][1]:
            prev_day, _ = stack.pop()
            answer[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))

    return answer


print(temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(temperatures([30, 40, 50, 60]))
print(temperatures([30, 60, 90]))
