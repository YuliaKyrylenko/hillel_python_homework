list_1 = [1, 2, 3, 4, 5, 6]

if len(list_1) % 2 == 0:
    num_id = len(list_1) // 2
else:
    num_id = len(list_1) // 2 + 1
list_2 = [list_1[:num_id], list_1[num_id:]]
print(list_2)