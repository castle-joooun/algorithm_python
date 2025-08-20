# https://leetcode.com/problems/valid-parentheses/
def isValid(s: str) -> bool:
    queue = []
    for c in s:
        if c in ['(', '[', '{']:
            queue.append(c)
        else:
            if len(queue) == 0:
                return False

            temp = queue[-1]
            if temp not in ['(', '[', '{']:
                return False

            if (temp == '(' and c == ')') \
                    or (temp == '[' and c == ']') \
                    or (temp == '{' and c == '}'):
                queue.pop()
            else:
                return False

    return len(queue) == 0


print(isValid(']'))
