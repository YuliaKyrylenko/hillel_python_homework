number = input('Enter a number: ')

while len(number) > 1:
    result = 1
    for char in number:
        result *= int(char)
    number = str(result)
print(number)