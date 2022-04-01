def count_five(N, num):
    count = 0
    while N != 0:
        N //= num
        count += N
    return count


N, M = map(int, input().split())
print(min(count_five(N, 5) - count_five(M, 5) - count_five(N - M, 5),
      count_five(N, 2) - count_five(M, 2) - count_five(N - M, 2)))
