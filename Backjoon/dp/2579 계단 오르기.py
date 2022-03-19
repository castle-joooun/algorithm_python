'''
### 💡 풀이순서

> f(1)은 무조건 step[0]이고
f(2)는 step[1] + step[2],
f(3)은 max(step[1] + step[3], step[2] + step[3])이 된다.

cache에 쌓아주며 연속된 3개의 계단을 밟지 않으면서 마지막 계단을 밟는 방법을 찾으면 될 것 같다.

그러면 cache에는 내가 연속으로 밟은 회수도 카운트해줘야 할 것 같다.
>
'''

N = int(input())
d = [(0, 0)] + [int(input()) for _ in range(N)]

cache = [(0, 0) * (N + 1)]
cache[1] = (d[1], 1)
cache[2] = (d[1] + d[2], 2)


def f(n):
  if cache[n] != (0, 0):
    return cache[n]
  
  if f(n - 1)[1] != 2:
    temp1 = f(n - 1)[0] + d[n]
    temp2 = f(n - 2)[0] + d[n]

    if temp1 > temp2:
      cache[n] = (temp1, cache[n - 1][1] + 1)
    else:
      cache[n] = (temp2, cache[n - 2][1] + 1)
  else:
    value = f(n - 2)[0] + d[n]
    cache[n] = (value, cache[n - 2][1] + 1)

  return cache[n]


value, count = f(n)
print(value)
