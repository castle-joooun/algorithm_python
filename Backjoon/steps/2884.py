hour, minute = map(int, input().split())

minute -= 45
if minute < 0:
    hour = hour -1 if hour != 0 else 23
    minute += 60

print(hour, minute)