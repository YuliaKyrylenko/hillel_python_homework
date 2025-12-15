lst = [0, 1, 7, 2, 4, 8]
total = 0

for idx, element in enumerate(lst):
    if idx % 2 == 0:
        total += element * lst[-1]
print(total)