num_1 = float(input("Enter a first number: "))
num_2 = float(input("Enter a second number: "))
oper = input("Enter a operator ( +, -, *, / ): ")

if oper == "+":
    result = num_1 + num_2
elif oper == "-":
    result = num_1 - num_2
elif oper == "*":
    result = num_1 * num_2
elif oper == "/":
    if num_2 > 0:
        result = num_1 / num_2
    else :
        result = "Division by zero is not possible"
else:
    result = "You have entered an invalid operator"

print(result)