# arr size, plus num, repeat
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

print((numbers[-2]*(m//k)) + (numbers[-1] * (m - (m//k))))