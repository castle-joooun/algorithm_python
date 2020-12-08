# programmers 60057
def solution(s):
    length = int(1e9)
    before = ''
    now = ''
    cnt = 0
    str_len = ''
    str_num = 1
    for i in range(1, len(s) // 2):
        check = 0
        if len(s) % i == 0:
            check = len(s) // i
        else:
            check = (len(s) // i) + 1

        while cnt != check + 1:
            if len(s) >= i:
                now = s[cnt * i: (cnt + 1) * i]

                if now == before:
                    str_num += 1
                else:
                    if str_num > 1:
                        str_len += str(str_num) + before
                    else:
                        str_len += before
                    before = now
                    str_num = 1
            else:
                str_len += s[cnt * i:]

            cnt += 1

        if length > len(str_len):
            length = len(str_len)
            print(str_len)

        cnt = 0
        str_len = ''

    return length


s = input()
print(solution(s))