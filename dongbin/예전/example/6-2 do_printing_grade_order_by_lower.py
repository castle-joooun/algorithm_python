n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))


def setting(arr):
    return arr[1]


array = sorted(array, key=setting)

for student in array:
    print(student[0], end=" ")