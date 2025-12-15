lst = [0, 1, 0, 12, 3]
lst_1 = []

cnt = lst.count(0)
for element in lst:
    if element != 0:
        lst_1.extend([element])
lst_1.extend([0] * cnt)
lst = lst_1                # if we need to change the starting list
print(lst)