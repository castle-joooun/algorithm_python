def solution(food_times, k):
    i = 0

    while k > 0:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                continue
            food_times[i] -= 1
            k -= 1

    return 1 if len(food_times) - 1 == i else i + 1


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
