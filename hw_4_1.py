# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

lst = [1, 0, 13, 0, 0, 0, 5]
lst_1 = []

cnt = lst.count(0)
for j in lst:
    if j != 0:
        lst_1.extend([j])
lst_1.extend([0] * cnt)
lst = lst_1                # if we need to change the starting list
print(lst)