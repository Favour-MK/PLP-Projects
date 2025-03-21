num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation sign to be done: ")
if operation == "+":
    print(num1 + num2) 
elif operation == "-":
    print(num1 - num2) 
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Invalid operation sign")

