from random import randint

random_lst = [randint(1, 100) for numbers in range(randint(3, 10))]
lst = [random_lst[element] for element in [0, 2, -2]]

print(random_lst)
print(lst)