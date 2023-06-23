# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    fib_series = []
    a, b = 0, 1

    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b

    return fib_series

# Display Fibonacci series up to 10 terms
fibonacci_series = fibonacci(10)
print("Fibonacci series up to 10 terms:")
print(fibonacci_series)
