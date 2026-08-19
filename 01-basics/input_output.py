# ==========================================
# Python Input & Output
# ==========================================


# ------------------------------------------
# 1. Basic Output
# ------------------------------------------

print("Hello, Python!")
print("I am learning Python.")


# ------------------------------------------
# 2. Output with Variables
# ------------------------------------------

name = "Hedaetullah"
age = 25

print("Name:", name)
print("Age:", age)


# ------------------------------------------
# 3. Formatted Output using f-string
# ------------------------------------------

print(f"My name is {name} and I am {age} years old.")


# ------------------------------------------
# 4. Taking String Input
# ------------------------------------------

user_name = input("Enter your name: ")

print(f"Hello, {user_name}!")


# ------------------------------------------
# 5. Taking Integer Input
# ------------------------------------------

user_age = int(input("Enter your age: "))

print(f"You are {user_age} years old.")


# ------------------------------------------
# 6. Taking Float Input
# ------------------------------------------

cgpa = float(input("Enter your CGPA: "))

print(f"Your CGPA is {cgpa}")


# ------------------------------------------
# 7. Taking Multiple Inputs
# ------------------------------------------

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Full Name: {first_name} {last_name}")


# ------------------------------------------
# 8. Taking Numbers and Performing Calculation
# ------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")


# ------------------------------------------
# 9. Using sep
# ------------------------------------------

print("Python", "JavaScript", "Java", sep=" | ")


# ------------------------------------------
# 10. Using end
# ------------------------------------------

print("Learning", end=" ")
print("Python")


# ------------------------------------------
# 11. Escape Characters
# ------------------------------------------

print("Name:\tHedaetullah")
print("Python\nProgramming")


# ------------------------------------------
# 12. Checking Input Data Type
# ------------------------------------------

age_input = input("Enter your age again: ")

print(f"Your input is: {age_input}")
print(f"Data type: {type(age_input)}")


# ------------------------------------------
# 13. Converting String Input to Integer
# ------------------------------------------

age_number = int(age_input)

print(f"Your age is: {age_number}")
print(f"Data type after conversion: {type(age_number)}")