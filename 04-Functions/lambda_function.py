 # ==========================================
# PYTHON LAMBDA FUNCTIONS - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. BASIC LAMBDA FUNCTION ===")
# Traditional function vs Lambda function
def square_def(n):
    return n ** 2

square_lambda = lambda n: n ** 2

print(f"Square using def: {square_def(5)}")
print(f"Square using lambda: {square_lambda(5)}")


print("\n=== 2. LAMBDA WITH MULTIPLE ARGUMENTS ===")
# Lambda taking multiple parameters
add = lambda a, b, c: a + b + c
multiply = lambda x, y: x * y

print(f"Sum of (10, 20, 30): {add(10, 20, 30)}")
print(f"Multiply 6 x 7: {multiply(6, 7)}")


print("\n=== 3. LAMBDA WITH CONDITIONAL EXPRESSION (IF-ELSE) ===")
# Syntax: lambda arg: true_value if condition else false_value
check_max = lambda a, b: a if a > b else b
check_even = lambda num: "Even" if num % 2 == 0 else "Odd"

print(f"Max between 15 and 25: {check_max(15, 25)}")
print(f"Check 7 is: {check_even(7)}")


print("\n=== 4. LAMBDA WITH MAP() & FILTER() ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map() to double every number
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"Doubled List: {doubled_numbers}")

# Using filter() to get only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filtered Evens: {even_numbers}")


print("\n=== 5. LAMBDA WITH CUSTOM SORTING ===")
# Sorting a list of tuples based on the second item (Age)
students = [("Rahim", 22), ("Karim", 19), ("Jubaer", 25)]

# Sort by age (index 1)
students_sorted_by_age = sorted(students, key=lambda student: student[1])
print("Sorted by Age:")
for name, age in students_sorted_by_age:
    print(f"Name: {name}, Age: {age}")