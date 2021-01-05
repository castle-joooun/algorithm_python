import heapq

d = []

while True:
    num = int(input())

    if num == -1:
        break
    if num == 0:
        print(heapq.heappop(d))
        d.clear()
    else:
        heapq.heappush(d, num)
