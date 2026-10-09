# ==========================================
# PYTHON SETS - COMPREHENSIVE GUIDE
# ==========================================

print("=== 1. SET CREATION & AUTOMATIC DUPLICATE REMOVAL ===")
# Set automatically removes duplicate items
numbers_set = {1, 2, 2, 3, 4, 4, 4, 5}
print(f"Set values (duplicates removed): {numbers_set}")

# Removing duplicates from a list using set()
raw_list = ["apple", "banana", "apple", "cherry", "banana"]
unique_fruits = list(set(raw_list))
print(f"Unique fruits list: {unique_fruits}")


print("\n=== 2. ADDING AND REMOVING ELEMENTS ===")
skills = {"Python", "Git"}

# Adding items
skills.add("VS Code")               # Adds a single item
skills.update(["SQL", "Django"])     # Adds multiple items
print(f"Updated Skills: {skills}")

# Removing items
skills.remove("SQL")                 # Removes item (raises KeyError if not found)
skills.discard("Java")               # Removes item safely (NO error if not found)
popped_skill = skills.pop()          # Removes an arbitrary item
print(f"Popped item: {popped_skill}")
print(f"Skills after removal: {skills}")


print("\n=== 3. MATHEMATICAL SET OPERATIONS ===")
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# Union: Combined items from both sets
print(f"Union (A | B): {set_A | set_B}")

# Intersection: Common items in both sets
print(f"Intersection (A & B): {set_A & set_B}")

# Difference: Items in A but NOT in B
print(f"Difference (A - B): {set_A - set_B}")

# Symmetric Difference: Items in either A or B, but NOT in both
print(f"Symmetric Difference (A ^ B): {set_A ^ set_B}")


print("\n=== 4. SET SUBSET AND SUPERSET CHECKING ===")
small_set = {1, 2}
big_set = {1, 2, 3, 4, 5}

print(f"Is small_set a subset of big_set? {small_set.issubset(big_set)}")
print(f"Is big_set a superset of small_set? {big_set.issuperset(small_set)}")
print(f"Are sets disjoint (no common items)? {small_set.isdisjoint({9, 10})}")