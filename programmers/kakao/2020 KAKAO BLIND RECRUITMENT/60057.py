def solution(s):
    answer = int(1e9)

    for num in range(1, len(s) + 1):
        before = s[:num]
        check = ''
        count = 1

        for i in range(num * 2, len(s) + 1, num):
            after_num = i - num

            # 이전 문자열이랑 같으면 카운트 up 후 continue
            if s[after_num:i] == before:
                count += 1
                continue

            check += str(count) + before if count != 1 else before
            count = 1
            before = s[after_num:i]

        check += str(count) + before if count != 1 else before
        check += s[(len(s) // num) * num:]
        answer = min(answer, len(check))

    return answer
