def check(i, j, d):
    ho, ver = '', ''
    ho_ori, ver_ori = '', ''
    for n in range(4, -1, -1):
        ho += str(d[i][j + n])
        ver += str(d[i + n][j])
    for n in range(5):
        ho_ori += str(d[i][j + n])
        ver_ori += str(d[i + n][j])

    print(ho, ho_ori)
    print(ver, ver_ori)
    if ho == ho_ori and ver == ver_ori:
        return 2
    elif ho == ho_ori or ver == ver_ori:
        return 1
    else:
        return 0


d = [list(map(int, input().split())) for _ in range(7)]

result = 0
for i in range(7 - 5):
    for j in range(7 - 5):
        result += check(i, j, d)

print(result)

# 두개로 나눠서 검사하기??
# 뭘 두개로 나눠서 생각하는거지
# 좀 더 고민해보기!