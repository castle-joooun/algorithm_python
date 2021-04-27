s = input()

one = 0
zero = 0

num = s[0]
for i in range(1, len(s)):
    if num != s[i]:
        num = s[i]
        if s[i] == '0':
            zero += 1
        else:
            one += 1

print(min(zero, one))
