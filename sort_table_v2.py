list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]

list_to_sort.sort(key=lambda x: x[2])
for i in range(0, len(list_to_sort) - 1):
    if list_to_sort[i][1] > list_to_sort[i + 1][1]:
        list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]

print(list_to_sort)
