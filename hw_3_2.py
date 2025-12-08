list_1 = [12, 3, 4, 10, 8]

#list_1 = list_1[-1:] + list_1[:-1] #old_variant

if len(list_1) > 1:
    last_element = list_1.pop(-1)
    list_1.insert(0, last_element)

print(list_1)