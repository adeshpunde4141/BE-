import time

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()  # To move to the next line after printing the series

n = int(input("Enter nth Fibonacci term: "))

start_time = time.time()
fibonacci(n)
end_time = time.time()

print(f"Execution time: {end_time - start_time:.6f} seconds")
