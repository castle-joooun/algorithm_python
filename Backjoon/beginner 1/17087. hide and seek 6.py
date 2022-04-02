from itertools import combinations

N, S = map(int,input().split())
l = list(map(int, input().split()))

if len(l) == 1:
    print(abs(l[0] - S))
else:
    check = [abs(a - b) for a, b in list(combinations(l, 2))]


    def find_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a


    gcd_arr = check[0]
    for i in range(len(check)):
        gcd_arr = find_gcd(gcd_arr, check[i])

    print(gcd_arr)