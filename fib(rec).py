import time

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

n = int(input("Enter nth Fibonacci term: "))
start_time = time.time()
fib_series = fibonacci(n)
end_time = time.time()

print(f"Fibonacci series up to {n} numbers:", fib_series)
print(f"Execution time: {end_time - start_time:.6f} seconds")
