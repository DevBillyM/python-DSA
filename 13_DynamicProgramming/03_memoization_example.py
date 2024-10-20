# Memoization Example using functools.lru_cache for Fibonacci

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testing Fibonacci with memoization
n = 10
print(f"Fibonacci sequence at position {n} is {fibonacci(n)}")  # Output: 55
