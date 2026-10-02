# ==========================================
# PYTHON FUNCTIONS - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. BASIC FUNCTION DEFINITION & CALL ===")
# Defining a simple function
def greet_user():
    print("Hello! Welcome to Python Functions.")

# Calling the function
greet_user()


print("\n=== 2. FUNCTION WITH PARAMETERS & RETURN VALUE ===")
# Function with parameters that returns a result
def add_numbers(a, b):
    result = a + b
    return result

# Calling function and storing returned value
sum_result = add_numbers(15, 25)
print(f"15 + 25 = {sum_result}")


print("\n=== 3. DEFAULT PARAMETER VALUES ===")
# Default value for 'country' is set to 'Bangladesh'
def display_profile(name, country="Bangladesh"):
    print(f"Name: {name} | Country: {country}")

display_profile("Jubaer")               # Uses default country
display_profile("John", "Canada")       # Overrides default country


print("\n=== 4. COMBINING FUNCTIONS WITH CONDITIONALS ===")
# Function checking number status
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

print(check_even_odd(10))
print(check_even_odd(7))


print("\n=== 5. VARIABLE-LENGTH ARGUMENTS (*ARGS & **KWARGS) ===")
# *args receives multiple positional arguments as a Tuple
def calculate_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of (5, 10, 15): {calculate_sum(5, 10, 15)}")
print(f"Sum of (1, 2, 3, 4, 5): {calculate_sum(1, 2, 3, 4, 5)}")

# **kwargs receives key-value pairs as a Dictionary
def print_user_details(**details):
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

print("\nUser Details:")
print_user_details(name="Rahim", age=22, role="Developer")