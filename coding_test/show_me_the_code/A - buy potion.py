import sys

input = sys.stdin.readline

N = int(input())
price = list(map(int, input().split()))
sale = []
for i in range(N):
    sale.append([])
    for _ in range(int(input())):
        sale[i].append(tuple(map(int, input().split())))

count = 0
coin = 0
check = [[price[i], len(sale[i]), False, i] for i in range(N)]
while count != N:
    check_sort = sorted(check, key=lambda x: (x[2], x[0], x[1]))
    coin += check_sort[0][0]
    check[check_sort[0][3]][2] = True
    count += 1

    for idx, coin_sale in sale[check[check_sort[0][3]][3]]:
        check[idx - 1][0] -= coin_sale
        if check[idx - 1][0] < 1:
            check[idx - 1][0] = 1

print(coin)