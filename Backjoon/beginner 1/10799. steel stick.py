pipe = input()

steel_count = 0
result = 0
index = 0
while index < len(pipe):
    if pipe[index] == '(':
        if pipe[index + 1] == ')':
            result += steel_count
            index += 1
        else:
            steel_count += 1
    else:
        steel_count -= 1
        result += 1

    index += 1
print(result)
