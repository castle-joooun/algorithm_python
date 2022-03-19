'''
### 💡 풀이순서

> max를 활용하여 제일 큰 수를 골라내면 된다.
근데 어디서부터 더하고, 어디서 끝마치고 하는 것이 어렵게 느껴졌다.

그래서 cache보다는 그냥 sum_list를 만들어 각 자리를 돌며 지금까지 합한 값, 현재값을 비교해서 append해주고 나중에 max로 제일 큰 값을 고르면 되지 않을까 싶었다.
> 

### 🔥 점화식

$$
f(n) = \max (sum[i] + d(i+1), d[i + 1])
$$
'''

n = int(input())
d = list(map(int, input().split()))

sum_list = [d[0]]

for i in range(n - 1):
  sum_list.append(max(sum_list[i] + d[i + 1], d[i + 1]))

print(max(sum_list))
