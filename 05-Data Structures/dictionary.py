# ==========================================
# PYTHON DICTIONARIES - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. DICTIONARY CREATION & ACCESSING VALUES ===")
# User profile dictionary
student = {
    "name": "Jubaer",
    "age": 22,
    "course": "Computer Science",
    "is_enrolled": True
}
print(f"Student Profile: {student}")

# Accessing values using Key and get() method
print(f"Name: {student['name']}")
# get() method prevents KeyError if the key doesn't exist
print(f"GPA: {student.get('gpa', 'Not Assigned')}")


print("\n=== 2. MODIFYING AND ADDING KEY-VALUE PAIRS ===")
# Updating existing key
student["age"] = 23

# Adding new key-value pair
student["gpa"] = 3.85
print(f"Updated Profile: {student}")


print("\n=== 3. REMOVING ELEMENTS ===")
# pop() removes specific key and returns its value
removed_gpa = student.pop("gpa")
print(f"Removed GPA: {removed_gpa}")

# popitem() removes the last inserted key-value pair
last_item = student.popitem()
print(f"Popped Last Item: {last_item}")
print(f"Profile after removals: {student}")


print("\n=== 4. LOOPING THROUGH DICTIONARIES ===")
inventory = {"Apples": 50, "Bananas": 30, "Oranges": 20}

print("--- Keys ---")
for key in inventory.keys():
    print(key, end=" ")

print("\n--- Values ---")
for value in inventory.values():
    print(value, end=" ")

print("\n--- Key-Value Pairs ---")
for item, count in inventory.items():
    print(f"{item}: {count} pcs")


print("\n=== 5. NESTED DICTIONARIES & DICTIONARY COMPREHENSION ===")
# Nested Dictionary
company = {
    "emp1": {"name": "Rahim", "role": "Developer"},
    "emp2": {"name": "Karim", "role": "Designer"}
}
print(f"Emp1 Role: {company['emp1']['role']}")

# Dictionary Comprehension (Squaring numbers)
# Syntax: {key: value for item in iterable if condition}
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares Dictionary: {squares}")