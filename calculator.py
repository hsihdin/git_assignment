def addition(a, b):
    # Add two numbers
    return a + b

def subtraction(a, b):
    # Subtract the second number from the first number
    return a - b

def multiplication(a, b):
    # Multiply two numbers
    return a * b

def division(a, b):
    # Divide the first number by the second number
    return a / b

# Sample input
num1 = 6
num2 = 4

# Perform calculations and print results
print("Calculator Program\n")
print(f"Sample input: {num1} and {num2}\n")

add_result = addition(num1, num2)
print(f"Addition: {num1} + {num2} = {add_result}")

sub_result = subtraction(num1, num2)
print(f"Subtraction: {num1} - {num2} = {sub_result}")

mul_result = multiplication(num1, num2)
print(f"Multiplication: {num1} * {num2} = {mul_result}")

div_result = division(num1, num2)
print(f"Division: {num1} / {num2} = {div_result}")
