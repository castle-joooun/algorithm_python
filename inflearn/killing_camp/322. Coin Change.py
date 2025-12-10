# https://leetcode.com/problems/coin-change/description/

from typing import List
from collections import deque


def coinChange(coins: List[int], amount: int) -> int:
    # ✅ 초기 금액을 amount, 동전 개수를 0으로 설정하고, 큐에 추가한다.
    queue = deque([(amount, 0)])
    visited = set()
    # ✅ 큐가 빌 때까지 반복문을 수행한다.
    while queue:
        # ✅ 큐에서 현재 남은 금액과 현재 동전 개수를 popleft한다.
        cur_amount, cur_coin = queue.popleft()
        # ✅ 현재 남은 금액이 0이라면 현재 동전 개수를 반환한다.
        if cur_amount == 0:
            return cur_coin

        # ✅ 한 동전을 사용해서 다음 남은 금액을 만든다.
        for c in coins:
            next_amount = cur_amount - c
            # ✅ 다음 남은 금액이 처음 발생하고, 액수가 0 이상이라면,
            if next_amount not in visited and next_amount >= 0:
                # ✅ visited에 다음 남은 금액을 추가한다.
                visited.add(next_amount)
                # ✅ 다음 남은 금액과 동전 개수에 1을 더해서 큐에 추가한다.
                queue.append((next_amount, cur_coin + 1))

    # ✅ coins의 동전으로 amount를 만들 수 없다면 -1을 반환한다.
    return -1


print(coinChange([1,2,5], 11))
