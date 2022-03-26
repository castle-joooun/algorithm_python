s = input()

check = False

result = ''
temp = ''


def split_list(string):
    string_list = list(string.split())

    for i in range(len(string_list)):
        string_list[i] = \
            ''.join(list(string_list[i])[::-1])

    return ' '.join(string_list)


for i in range(len(s)):
    if check:
        if s[i] == '>':
            check = False
        result += s[i]
        continue

    if s[i] == '<':
        check = True
        result += split_list(temp) + s[i]
        temp = ''
        continue

    temp += s[i]

result += split_list(temp)
print(result)