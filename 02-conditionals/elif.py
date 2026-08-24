# ==========================================
# PYTHON ELIF STATEMENT - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. BASIC IF-ELIF-ELSE CHAIN ===")
marks = 75

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 33:
    grade = "Pass"
else:
    grade = "Fail"

print(f"Marks: {marks} | Grade: {grade}")


print("\n=== 2. MULTIPLE IF VS ELIF (PERFORMANCE DIFFERENCE) ===")
temperature = 35

# Using multiple 'if' statements (Python checks EVERYTHING)
print("--- Using Multiple IF ---")
if temperature > 30:
    print("It's hot outside!")
if temperature > 20:
    print("It's warm outside!") # This also prints even though it's already hot!

# Using 'elif' (Python stops at the FIRST matching condition)
print("--- Using IF-ELIF Chain ---")
if temperature > 30:
    print("It's hot outside!") # Only this line runs!
elif temperature > 20:
    print("It's warm outside!")


print("\n=== 3. ELIF WITH LOGICAL OPERATORS & RANGES ===")
age = 25

if age < 0:
    print("Invalid age entered.")
elif age >= 0 and age <= 12:
    print("Category: Child")
elif 13 <= age <= 19:  # Chained comparison syntax in Python
    print("Category: Teenager")
elif age >= 20 and age < 60:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")


print("\n=== 4. MENU / CHOICE DRIVEN SYSTEM USING ELIF ===")
user_role = "editor"

if user_role == "admin":
    print("Access: Full System Control & Database Access")
elif user_role == "editor":
    print("Access: Create, Edit & Publish Articles")
elif user_role == "viewer":
    print("Access: Read Content Only")
else:
    print("Access: Guest User - Please Register")