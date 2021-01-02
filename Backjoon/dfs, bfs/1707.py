import sys
input = sys.stdin.readline

#다시 해보기~
def dfs(graph, v, visited):
    visited[v] = True
    color_check = 3 - color[v]
    for i in graph[v]:
        if color[v] == 0:
            color[v] = color_check
            dfs(graph, i, visited)
        elif color[v] == color_check:
            print('NO')
            break
    else:
        print('YES')


n = int(input())
for _ in range(n):
    v, e = map(int, input().split())
    d = [[] for _ in range(v + 1)]
    for i in range(e):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)

    # 색이 다르게 표시(1, 2)
    color = [0] * (v + 1)
    color[i] = 1
    l = [i]  # 시작값


    visited = [False] * (v + 1)
    dfs(d, 1, visited)
    '''
    check = False # 멈추는 요소
    for i in range(1, v + 1):
        if check:
            break
        if color[i] > 0: # 색은 1, 2만 들어감
            continue

        color[i] = 1
        l = [i] # 시작값

        # check가 True면 break
        # l이 empty면 break
        while l and not check:
            num = l.pop()
            color_check = 3 - color[num] # 1 또는 2가 되게 설정

            for x in d[num]:
                if color[x] == 0:
                    color[x] = color_check # 1 또는 2를 가지게 됌
                    l.append(x) # l을 추가하여 empty가 되지 않게
                elif color[x] == color[num]: # 색의 변화가 없음 -> 이분그래프가 아님
                    check = True
                    break

    print('NO' if check else 'YES')
    '''
