# https://leetcode.com/problems/longest-valid-parentheses/description/

def longestValidParentheses(s: str) -> int:
    answer = 0
    stack = [-1]

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                answer = max(answer, i - stack[-1])

    return answer


print(longestValidParentheses('()(()'))
