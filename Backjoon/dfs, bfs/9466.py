t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))

# dfs에서 돌리면서 해당되는 index를 리스트 변수에 append함
# visited True해줌
# if index in list라면 remove해줌
# if list[-1] == idex라면 remove해주고 남은수를 result에 더해줌!
# 풀릴것 같은데...?
