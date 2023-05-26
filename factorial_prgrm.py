def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input
num = int(input("Enter a number: "))

# Calculate factorial
result = factorial(num)

# Output
print(f"The factorial of {num} is {result}")

