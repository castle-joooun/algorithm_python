N = int(input())
l = list(map(int, input().split()))

result = [str(l[j])
          for i in range(N)
          for j in range(i + 1, N)
          if l[i] < l[j]
          ]

print(' '.join(result))
