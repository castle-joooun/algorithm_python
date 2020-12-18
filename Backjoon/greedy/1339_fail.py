# 같은 length를 가진 것들의 alpha를 모아서 가져옴
def check_num(alpha):
    small_point = []
    for k in range(len(alpha)):
        point = 0
        for i in range(n):
            for j in range(len(d[i])):
                if d[i][j] == alpha[k]:
                    point += d[i].find(alpha[k])
        small_point.append((point, alpha[k]))
    small_point.sort(key=lambda x:x[0])
    return small_point

def find_alpha(arr):
    for i in range(len(arr[0])):
        alpha = []
        for j in range(len(arr)):
            alpha.append(arr[j][i])




n = int(input())
d = []
length = [[] for i in range(8)]
for i in range(n):
    d.append(input())
    length[len(d[i])].append(i)

for i in range(8, 0, -1):
    if len(length[i]) == 0:
        continue
    if len(length[i]) > 1:
        for arr in length[i]:
            find_alpha(arr)
