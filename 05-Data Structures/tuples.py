# ==========================================
# PYTHON TUPLES - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. TUPLE CREATION AND SINGLE ITEM TUPLE ===")
# Basic Tuple
coordinates = (10.5, 20.8, 30.1)
print(f"Coordinates: {coordinates} | Type: {type(coordinates)}")

# Single Item Tuple Warning (Comma is required!)
not_a_tuple = ("Python")    # Treats as String
is_a_tuple = ("Python",)     # Treats as Tuple
print(f"Type without comma: {type(not_a_tuple)}")
print(f"Type with comma: {type(is_a_tuple)}")


print("\n=== 2. TUPLE INDEXING AND SLICING ===")
colors = ("Red", "Green", "Blue", "Yellow", "Orange")

print(f"First Color: {colors[0]}")
print(f"Last Color: {colors[-1]}")
print(f"Middle Colors (1 to 3): {colors[1:4]}")


print("\n=== 3. IMMUTABILITY & CONVERTING TO LIST ===")
point = (5, 10)
# point[0] = 15  --> Error! Tuples cannot be modified directly.

# Workaround: Convert to list, modify, then convert back to tuple
temp_list = list(point)
temp_list[0] = 15
point = tuple(temp_list)
print(f"Modified Tuple via List conversion: {point}")



print("\n=== 4. TUPLE UNPACKING ===")
person = ("Jubaer", 23, "Software Engineer")

# Unpacking elements into variables
name, age, profession = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")

# Extended Unpacking using *
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print(f"First: {first} | Middle: {middle} | Last: {last}")


print("\n=== 5. TUPLE METHODS & OPERATIONS ===")
sample_tuple = (1, 2, 3, 2, 4, 2, 5)

# Built-in Methods
print(f"Count of 2: {sample_tuple.count(2)}")
print(f"Index of value 4: {sample_tuple.index(4)}")

# Concatenation & Repetition
t1 = (1, 2)
t2 = (3, 4)
print(f"Combined Tuple: {t1 + t2}")
print(f"Repeated Tuple: {t1 * 3}")