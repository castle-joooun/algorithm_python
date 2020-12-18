import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    d.sort(key=lambda x:x[0])
    count = 1 # 서류심사 인원은 늘 통과
    grade = d[0][1]
    for i in range(1, n):
        grade = min(grade, d[i][1])
        if grade == d[i][1]:
            count += 1
    print(count)