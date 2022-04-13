N = int(input())
l = list(map(int, input().split()))

cnt = 0
last_num = 0
for i in range(N - 1):
    temp_cnt = 1
    last_num = l[i]
    if len(l[i:]) > cnt:
        for j in range(i + 1, N):
            if l[j] > last_num:
                last_num = l[j]
                temp_cnt += 1

        cnt = max(cnt, temp_cnt)

print(cnt)