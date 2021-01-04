def insert(d, dic):
    for x in d:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1


first = dict([])
second = dict([])
insert(input(), first)
insert(input(), second)

print('YES' if first == second else 'NO')