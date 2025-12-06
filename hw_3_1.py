num_1 = float(input("Enter a first number: "))
num_2 = float(input("Enter a second number: "))
oper = input("Enter a operator ( +, -, *, / ): ")

if oper == "+":
    print(num_1 + num_2)
elif oper == "-":
    print(num_1 - num_2)
elif oper == "*":
    print(num_1 * num_2)
elif oper == "/":
    if num_2 > 0:
        print(num_1 / num_2)
    else :
        print("Division by zero is not possible")
else:
    print("You have entered an invalid operator")