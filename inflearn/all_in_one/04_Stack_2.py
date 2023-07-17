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
