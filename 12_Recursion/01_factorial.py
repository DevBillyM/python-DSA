# Factorial Implementation using Recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Testing Factorial
n = 5
print(f"Factorial of {n} is {factorial(n)}")  # Output: 120
