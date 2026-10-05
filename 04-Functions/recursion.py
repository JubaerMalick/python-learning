# ==========================================
# PYTHON RECURSION - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. BASIC RECURSION (COUNTDOWN) ===")
def countdown(n):
    # Base Case: Stop when n reaches 0
    if n <= 0:
        print("Blastoff! 🚀")
        return
    
    print(f"Count: {n}")
    # Recursive Case: Call function with n - 1
    countdown(n - 1)

countdown(3)


print("\n=== 2. FACTORIAL USING RECURSION ===")
# Factorial formula: n! = n * (n - 1)!
def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    return n * factorial(n - 1)

number = 5
print(f"Factorial of {number} is: {factorial(number)}")


print("\n=== 3. FIBONACCI SERIES USING RECURSION ===")
# Fibonacci formula: fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    # Base Cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive Case
    return fibonacci(n - 1) + fibonacci(n - 2)

print("First 7 Fibonacci numbers:")
for i in range(7):
    print(fibonacci(i), end=" ")
print()


print("\n=== 4. SUM OF LIST ELEMENTS USING RECURSION ===")
def recursive_sum(numbers):
    # Base Case: Empty list returns 0
    if not numbers:
        return 0
    # Recursive Case: Head + sum of Tail
    return numbers[0] + recursive_sum(numbers[1:])

num_list = [10, 20, 30, 40]
print(f"Sum of {num_list} is: {recursive_sum(num_list)}")