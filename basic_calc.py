import math 
num1 = float(input("Enter first number: "))
operation = input("Enter operation which you want to perform (+, -, *, /): ")
num2 = float(input("Enter second number: "))
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    print("Invalid operation")
print(num1 , operation, num2, "=", result)