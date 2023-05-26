Calculator Program
This is a simple calculator program written in Python. It performs basic arithmetic operations such as addition, subtraction, multiplication, and division on two numbers.


Functions
### Addition

```
def addition(a, b):
    # Add two numbers
    return a + b
 
```

The addition function takes two numbers as input and returns their sum.


### Subtraction

```
def subtraction(a, b):
    # Subtract the second number from the first number
    return a - b
```

The subtraction function takes two numbers as input and returns the result of subtracting the second number from the first number.


### Multiplication

```
def multiplication(a, b):
    # Multiply two numbers
    return a * b
```

The multiplication function takes two numbers as input and returns their product.


### Division

```
def division(a, b):
    # Divide the first number by the second number
    return a / b
    ```
The division function takes two numbers as input and returns the result of dividing the first number by the second number.

Sample Input and Output
```
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
This section shows the sample input values of num1 and num2. It then performs the calculations using the defined functions and prints the results of addition, subtraction, multiplication, and division with the given sample input.
```
