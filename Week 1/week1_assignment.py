# Basic Calculator Program

# Ask user for the first number
num1 = float(input("Enter the first number: "))

# Ask user for the second number
num2 = float(input("Enter the second number: "))

# Ask user for the operation
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation based on the operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation. Please use +, -, *, or /.")
