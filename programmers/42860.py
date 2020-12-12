def solution(name):
    answer = 0
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

    def check(name, alpha, num):
        answer = 0
        for i in range(0, len(name), num):
            answer += 1 if i != 0 else 0
            if name[i] == 'A':
                continue

            min_plus = 0
            min_minus = 0
            while alpha[min_plus] != name[i]:
                min_plus += 1
            while alpha[min_minus] != name[i]:
                min_minus -= 1

            answer += min(min_plus, abs(min_minus))
        return answer

    return min(check(name, alpha, 1), check(name, alpha, -1))
