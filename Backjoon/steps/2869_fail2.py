a, b, v = map(int, input().split())

days = v // (a - b) - 1
now_v = (a - b) * days
print(days, now_v)

while True:
    now_v += a
    days += 1
    if now_v >= v:
        print(days)
        break
    now_v -= b