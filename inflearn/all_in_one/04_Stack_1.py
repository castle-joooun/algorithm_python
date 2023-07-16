def solv(s):
    stack = []
    check_dict = {'(': ')', '{': '}', '[': ']'}
    for x in s:
        if x in ['(', '{', '[']:
            stack.append(x)
        else:
            if not stack:
                return False

            if check_dict[stack.pop()] != x:
                return False
    return True


print(solv(')('))
print(solv('([]}'))
print(solv('{()[]}'))
