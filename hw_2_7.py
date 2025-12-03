number = int(input("Введіть число: "))

first_num, first_num_1 = divmod(number, 1000)
second_num, second_num_1 = divmod(first_num_1, 100)
third_num, fourth_num= divmod(second_num_1, 10)

print(first_num)
print(second_num)
print(third_num)
print(fourth_num)