d = input()
dd = ''
result = 0

i = 0
while i != len(d) - 1:
    if d[i] == '-':
        str_num = ''
        for j in range(i + 1,len(d)):
            if d[j] == '-':
                break
            i += 1
            str_num += d[j]
        make_num = ''
        add_num = 0
        for j in range(len(str_num)):
            if str_num[j] == '+':
                add_num += int(make_num)
                make_num = ''
            else:
                make_num += str_num[j]
        dd += "-" + str(int(make_num) + add_num)
    else:
        if i == 0:
            dd += '+'
        dd += d[i]
        i += 1

def plus_minus(index, data, cal, result):
    check = ''
    for i in range(index + 1, len(data)):
        if data[i] == '-' or data[i] == '+':
            break
        else:
            check += data[i]
    if cal == '+':
        return result + int(check)
    else:
        return result - int(check)


for i in range(len(dd)):
    if dd[i] == '+' or dd[i] == '-':
        result = plus_minus(i, dd, dd[i], result)
        check = ''
    else:
        check += dd[i]

print(result)