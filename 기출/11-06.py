def food_mekbang(foods, k):
    time = 0
    index = 0
    food = 0

    while time != k:
        while True:
            if foods[index] == 0:
                index += 1
                continue
            else:
                foods[index] -= 1
                index += 1
                break

        time += 1

        if index == len(foods):
            index = 0
        food = index

    return food + 1


foods = [3, 1, 2]
k = 5

print(food_mekbang(foods, k))