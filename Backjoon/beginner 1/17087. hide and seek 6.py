def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


N, S = map(int,input().split())
l = list(map(int, input().split()))
check = list(set(abs(l[i] - S) for i in range(N)))

gcd_arr = check[0]
for i in range(len(check)):
    gcd_arr = find_gcd(gcd_arr, check[i])

print(gcd_arr)