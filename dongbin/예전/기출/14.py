def solution(n, weak, dist):
    # n 미터, weak 취약한 부분(list), dist 친구들이 이동할 수 있는 거리(list)
    for i in range(len(weak)):
        for j in range(len(dist)):
            right = weak[i] + dist[-(i + 1)]
            left = weak[i] - dist[-(i + 1)]
    answer = 0
    return answer