def insert(d, dic):
    for x in d:
        dic[x] = dic.get(x, 0) + 1


first = dict()
second = dict()
insert(input(), first)
insert(input(), second)

print('YES' if first == second else 'NO')