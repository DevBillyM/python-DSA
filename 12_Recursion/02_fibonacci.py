# Fibonacci Sequence Implementation using Recursion

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testing Fibonacci
n = 10
print(f"Fibonacci sequence at position {n} is {fibonacci(n)}")  # Output: 55
