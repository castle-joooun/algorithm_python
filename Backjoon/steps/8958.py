n = int(input())

for _ in range(n):
    quiz = input()
    o_score = 0
    result = 0
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            o_score += 1
        else:
            o_score = 0
        result += o_score

    print(result)