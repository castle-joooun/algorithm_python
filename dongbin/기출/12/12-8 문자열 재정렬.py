n = input()

string = ''
number = 0

for x in n:
    if 'A' <= x <= 'Z':
        string += x
    else:
        number += int(x)

string = ''.join(sorted(list(map(str, string))))
result = string + str(number)
print(result)
