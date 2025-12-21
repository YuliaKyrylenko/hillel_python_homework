from string import ascii_letters

letters = input("Please enter two letters separated by a hyphen: ").split("-")

result = ascii_letters[ascii_letters.find(letters[0]):ascii_letters.find(letters[-1])+1]
print(f'{result}')