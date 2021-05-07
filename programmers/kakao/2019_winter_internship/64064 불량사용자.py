from itertools import combinations


def solution(user_id, banned_id):
    result = []
    tests = sorted(list(combinations(user_id, len(banned_id))))

    for test in tests:
        check = []
        for ban in banned_id:
            for user in test:
                if len(ban) != len(user):
                    continue
                if user in check:
                    continue

                for i in range(len(ban)):
                    if ban[i] == '*':
                        continue
                    if ban[i] != user[i]:
                        break
                else:
                    check.append(user)
                    break

        if len(check) == len(banned_id):
            check.sort()
            result.append(check)

    return len(result)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
               ["*rodo", "*rodo", "******"]))
