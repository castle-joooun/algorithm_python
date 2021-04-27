n = input()

mid = len(n) // 2
front = n[:mid]
back = n[mid:]

if sum(list(map(int, front))) == sum(list(map(int, back))):
    print('LUCKY')
else:
    print('READY')
