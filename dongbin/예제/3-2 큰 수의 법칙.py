def solution(arr, m, k):
    answer = 0

    arr.sort()
    max1, max2 = arr.pop(), arr.pop()

    answer = (max1 * k + max2) * (m // (k + 1)) + max1 * (m % (k + 1))

    return answer


print(solution([2, 4, 5, 4, 6], 8, 3))
