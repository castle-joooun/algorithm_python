def solution(numbers, hand):
    answer = ''

    clicks = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0],
              [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

    left = [3, 0]
    right = [3, 2]

    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            left = clicks[numbers[i]]
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            right = clicks[numbers[i]]
        else:
            left_abs = abs(left[0] - clicks[numbers[i]][0]) + \
                abs(left[1] - clicks[numbers[i]][1])
            right_abs = abs(right[0] - clicks[numbers[i]][0]) + \
                abs(right[1] - clicks[numbers[i]][1])

            if left_abs == right_abs:
                if hand == 'right':
                    answer += 'R'
                    right = clicks[numbers[i]]
                else:
                    answer += 'L'
                    left = clicks[numbers[i]]
            elif left_abs > right_abs:
                answer += 'R'
                right = clicks[numbers[i]]
            else:
                answer += 'L'
                left = clicks[numbers[i]]

    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
