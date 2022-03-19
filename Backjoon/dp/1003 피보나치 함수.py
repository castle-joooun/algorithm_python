'''
### 💡 풀이순서

> 간단해 보인다. f(n)이 f(n-1) + f(n-2)이기 때문에 각각의 경우때 0과 1일때를 알아내기만 하면 될 것 같다.
> 

### 🔥 점화식

$$
f(n) = f(n-1) + f(n-2)
$$
'''

cache = [[0, 0] for _ in range(40)]
cache[0] = [1, 0]
cache[1] = [0, 1]


def f(n):
  if cache[n] != [0, 0]:
    return cache[n]

  for i in range(2):
    cache[n][i] += f(n - 1)[i] + f(n - 2)[i]
  
  return cache[n]


for _ in range(int(input())):
  N = int(input())

  result = f(N)
  print(f'{result[0]} {result[1]}')
